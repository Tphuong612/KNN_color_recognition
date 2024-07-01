import math
import csv
import os

#Tính toán khoảng cách Eulid giữa 2 mẫu với length là số đặc trưng của 1 mẫu
def calculateDistance(var1, var2):
    '''
    #Tính toán khoảng cách Eulid giữa 2 mẫu với length là số đặc trưng của 1 mẫu
    var1: mẫu 1
    var2: mẫu 2
    length: số lượng đặc trưng của 1 mẫu
    '''
    length= 3 # Do một mau co 3 he mau (RGB)
    distance = 0
    for i in range(length):
        distance += pow((var1[i] - var2[i]), 2)
    return math.sqrt(distance)

#Lấy K láng giềng gần nhất
def k_NearestNeighbors(training_data, test_instance, k): #thêm tham số k
    '''
    Tìm k láng giêng gần nhất đối với 1 tập dữ liệu mới
    training_feature_vector: các mẫu đã có trong tập dữ liệu
    testIntance: mẫu mới cần xác định nhãn
    k: số lượng láng giềng
    '''
    list_neighbor =[] # list chua cac tuple voi gia tri dau la label, gia tri 2 la khoang cach
    for x in training_data: 
        distance = calculateDistance(x, test_instance) # Lan luot tinh khoang cach giua du lieu 
        list_neighbor.append((x[-1], distance))
    list_neighbor.sort(key=lambda x: x[1])
    return list_neighbor[:k] # Tra ve k tuple dau tien


def findMostOccur(list_neighbor): 
    frequency = {} # 1 dict luu tan suat xuat hien
    for neighbor in list_neighbor:
        if neighbor[0] in frequency:
            frequency[neighbor[0]] +=1
        else:
            frequency[neighbor[0]] = 1
            
    # Sap xep theo tan suat xuat hien
    res = sorted(frequency.items(), key= lambda x: x[1], reverse= True) 
    return res[0][0] # Tra ve gia tri dau tien cua dict (label)


def loadData(path):
    """
    Ham isfile(): Kiem tra lieu mot duong dan cho truoc co ton tai hay khong
    Ham os.access(path, mode): kiem tra kha nang truy cap cua mot file nao do
        + Return True or False
        + Cac Mode: 
            R_OK: read permission
            F_OK: Existence
            W_OK: Write permission
    """
    if os.path.isfile(path) and os.access(path, os.R_OK):
        with open(path) as csvfile:
            lines = csv.reader(csvfile)
            data = list(lines) # Chuyen file csv ve dang list 2 chieu

            if 'training' in path:
                data.pop(0) # Xoa header neu la tap training
                
            for x in range(len(data)):
                for y in range(3):
                    data[x][y] = float(data[x][y])
            return data
        
# loadData('./training_dataset/data.csv')


def main(training_path, testing_path, k): #thêm tham số k
    '''
    Hàm này đánh giá model với số láng giềng k
    training_path: đường dẫn đến file lưu các đặc trưng của tập Training (đã gán nhãn)
    testing_path: đương dẫn đến file luu các đăch trưng của tập Test (chưa có nhãn)
    '''
    training_vector=[]
    testing_vector = []

    training_vector = loadData(training_path)
    testing_vector = loadData(testing_path)
    black0, blue0, brown0, grey0, green0, orange0, pink0, purple0, red0, white0, yellow0 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
    for i in range(len(testing_vector)): #đếm số lượng các mẫu thực sự thuộc lớp đó
        if testing_vector[i][-1] == 'Black': black0 += 1 #đếm số lượng số các mẫu được phân vào các nhãn lớp
        elif testing_vector[i][-1] == 'Blue': blue0 += 1
        elif testing_vector[i][-1] == 'Brown': brown0 += 1
        elif testing_vector[i][-1] == 'Grey': grey0 += 1
        elif testing_vector[i][-1] == 'Green': green0 += 1
        elif testing_vector[i][-1] == 'Orange': orange0 += 1
        elif testing_vector[i][-1] == 'Pink': pink0 += 1
        elif testing_vector[i][-1] == 'Purple': purple0 += 1
        elif testing_vector[i][-1] == 'Red': red0 += 1
        elif testing_vector[i][-1] == 'White': white0 += 1
        elif testing_vector[i][-1] == 'Yellow': yellow0 += 1 
    # print(black0, blue0, brown0, grey0, green0, orange0, pink0, purple0, red0, white0, yellow0)
    # k = 6

    cnt =0
    black, blue, brown, grey, green, orange, pink, purple, red, white, yellow = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    black1, blue1, brown1, grey1, green1, orange1, pink1, purple1, red1, white1, yellow1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    prediction=[]
    for i in range(len(testing_vector)):
        list_neighbor = k_NearestNeighbors(training_vector, testing_vector[i], k)
        result = findMostOccur(list_neighbor)
        prediction.append(result)
        if result == testing_vector[i][-1]: #đếm tổng số lượng dự đoán đúng
            cnt +=1
        
        #     print(str(i+1)+ ' '+ str(testing_vector[i]) + '-->'+result)    
        # else:
        #     print(str(i+1)+ ' '+ str(testing_vector[i]) + '-->'+result + '(Wrong)')   
        
        if result == 'Black': black += 1 #đếm số lượng số các mẫu được phân vào các nhãn lớp
        elif result == 'Blue': blue += 1
        elif result == 'Brown': brown += 1
        elif result == 'Grey': grey += 1
        elif result == 'Green': green += 1
        elif result == 'Orange': orange += 1
        elif result == 'Pink': pink += 1
        elif result == 'Purple': purple += 1
        elif result == 'Red': red += 1
        elif result == 'White': white += 1
        elif result == 'Yellow': yellow += 1    
        
        if result == "Black" and result == testing_vector[i][-1]: black1 += 1 #số lượng các mẫu được phân loại đúng vào các nhãn lớp
        elif result == 'Blue' and result == testing_vector[i][-1]: blue1 += 1
        elif result == 'Brown' and result == testing_vector[i][-1]: brown1 += 1
        elif result == 'Grey' and result == testing_vector[i][-1]: grey1 += 1
        elif result == 'Green' and result == testing_vector[i][-1]: green1 += 1
        elif result == 'Orange' and result == testing_vector[i][-1]: orange1 += 1
        elif result == 'Pink' and result == testing_vector[i][-1]: pink1 += 1
        elif result == 'Purple' and result == testing_vector[i][-1]: purple1 += 1
        elif result == 'Red' and result == testing_vector[i][-1]: red1 += 1
        elif result == 'White' and result == testing_vector[i][-1]: white1 += 1
        elif result == 'Yellow' and result == testing_vector[i][-1]: yellow1 += 1
        
    m0 = [black0, blue0, brown0, grey0, green0, orange0, pink0, purple0, red0, white0, yellow0]
    m =  [black, blue, brown, grey, green, orange, pink, purple, red, white, yellow]   
    m1 = [black1, blue1, brown1, grey1, green1, orange1, pink1, purple1, red1, white1, yellow1]
    # print(black, blue, brown, grey, green, orange, pink, purple, red, white, yellow)   
    # print(black1, blue1, brown1, grey1, green1, orange1, pink1, purple1, red1, white1, yellow1)       
    # print('Acurency: '+ f'{cnt/len(testing_vector) * 100:.2f}')
    color = ['black', 'blue', 'brown', 'grey', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow']
    # print(*m0)
    # print(*m)
    # print(*m1)
    avg_precision = 0
    avg_recall = 0
    avg_f1score = 0
    print('\n\n')
    for i in range(11):
        precision = m1[i]/m[i]*100
        recall = m1[i]/m0[i]*100
        f1_score = 2*(precision*recall)/(precision+recall)
        avg_precision += precision
        avg_recall += recall
        avg_f1score += f1_score
        print(f'{color[i]}:\n\tPrecision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {f1_score:.2f}')
    # print('Acurency: '+ str(cnt/len(testing_vector) * 100), end=", ")
    print('Acurency: '+ f'{cnt/len(testing_vector) * 100:.2f}', end=", ")
    print(f'Avarage Precision: {avg_precision/11:.2f}, Avarage Recall: {avg_recall/11:.2f}, Avarage F1_score: {avg_f1score/11:.2f}')
    # print()
    # print(prediction) 
    # print(testing_vector)
    # print(type(training_vector))
    print('\n\n')
def classify_img(testing_path): #dùng cho mẫu dữ liệu predict
    training_vector=[]
    testing_vector = []

    training_vector = loadData('./training_dataset/data.csv')
    testing_vector = loadData(testing_path)
    # print(testing_vector)
    # k=6
    list_neighbor = k_NearestNeighbors(training_vector, testing_vector[0], 9)
    result = findMostOccur(list_neighbor)
    # print(result)
    return result


# #tìm giá trị k phù hợp cho mô hình
# for i in range(5, 30):
#     print(f'k={i} có', end=" ")
#     main('./training_dataset/data.csv', './testing_dataset/testing.data', k=i)


# l = ['black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow']
# for i in l:
#     path_test = './testing_dataset/' + i
#     print(f'{i}: ', sep=" ")
#     main('./training_dataset/data.csv', path_test, 6)
main('./training_dataset/data.csv', "./testing_dataset/testing.data", 6)
# classify_img('./testing_dataset/testing_image.data')

