
d = {'a': 2, 'b': 1, 'c': 4, 'd': 5}
print(d)
d= sorted(d.items(), key= lambda x: x[1], reverse= True)
print(d)
print(d[0][0])