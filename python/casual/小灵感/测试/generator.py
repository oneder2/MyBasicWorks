lst = [1,2,3,4,5]
g = (i for i in lst if i in lst)
lst = [0,1,2]
print(list(g))
