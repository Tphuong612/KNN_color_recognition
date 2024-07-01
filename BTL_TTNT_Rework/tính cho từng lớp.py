import os
import cv2
import numpy as np
# from color_recognition_api import KNN

def color_histogram_of_test_image(test_src_image):
    '''
    Trích xuất đặc tưng màu RGB để đem đi dự đoán
    '''

    # load the image
    image = test_src_image

    chans = cv2.split(image) #chia ảnh thành các kênh màu, theo cv2 thì là 3 kênh màu theo thứ tự BGR
    colors = ('b', 'g', 'r') #tên các kênh màu

    feature_data = '' #chứa đặc trưng màu của 1 ảnh
    counter = 0 #có vai trò để kiểm tra đang ở kênh màu nào
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        #hist = cv2.calcHist(images, channels, mask, hitSize, ranges)

        elem = np.argmax(hist) #trả về chỉ số màu có tần suất xuất hiện cao nhất trong histogram.

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            # print(feature_data)

    # Mo file va ghi de len file data
    with open('./testing_dataset/testing_image.data', 'w') as myfile:
        myfile.write(feature_data)


def color_histogram_of_image(img_name):
    '''
    Hàm này để tính toán các histogram của 1 ảnh tên img_name theo RGB 
    và sau đó được ghi vào tệp traning.data cùng với nhãn mô tả của nó
    '''
    
    # gán nhãn cho các file: nếu tên ảnh/đường dẫn chứa màu nào thì sẽ gán nhãn của ảnh đó là màu ý
    label =''
    for file_name in os.listdir('./testing_image'): 
        if(file_name in img_name):
            label = file_name
            break
        
    # load the image
    image = cv2.imread(img_name) #Đọc ảnh từ đường dẫn 'img_name' bằng OpenCV
    chans = cv2.split(image) #Tach anh mau thanh cac kenh mau B, G, R để lấy đặc trưng
    colors = ('b', 'g', 'r')
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        elem = np.argmax(hist) #lấy giá trị mức xám cao nhất
        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
    with open('./testing_dataset/pink', 'a') as myfile:
        myfile.write(feature_data + ',' + label + '\n')


def feature_test(): 
    '''
    hàm này để gán nhãn cho tất cả cac ảnh
    đồng thời nó sử dụng hàm color_histogram_of_image(img_name) để trích xuất các histogram 
    '''
    # for f in os.listdir('./testing_image/Black'):    # black color test images
    #     color_histogram_of_image('./testing_image/Black/' + f)
    # for f in os.listdir('./testing_image/Blue'):    # blue color test  images
    #     color_histogram_of_image('./testing_image/Blue/' + f)		
    # for f in os.listdir('./testing_image/Brown'):    # brown color test  images
    #     color_histogram_of_image('./testing_image/Brown/' + f)		
    # for f in os.listdir('./testing_image/Green'):    # green color test  images
    #     color_histogram_of_image('./testing_image/Green/' + f)
    # for f in os.listdir('./testing_image/Grey'):    # grey color test  images
    #     color_histogram_of_image('./testing_image/Grey/' + f)	
    # for f in os.listdir('./testing_image/Orange'):    # orange color test  images
    #     color_histogram_of_image('./testing_image/Orange/' + f)
    # for f in os.listdir('./testing_image/Red'):    # red color test  images
    #     color_histogram_of_image('./testing_image/Red/' + f)
    # for f in os.listdir('./testing_image/Purple'):    # purple color test  images
    #     color_histogram_of_image('./testing_image/Purple/' + f)	
    # for f in os.listdir('./testing_image/White'):    # white color test  images
    #     color_histogram_of_image('./testing_image/White/' + f)
    # for f in os.listdir('./testing_image/yellow'):    # yellow color test  images
    #    color_histogram_of_image('./testing_image/Yellow/' + f)
    for f in os.listdir('./testing_image/Pink'):    # pink color test  images
       color_histogram_of_image('./testing_image/Pink/' + f)
       
feature_test()