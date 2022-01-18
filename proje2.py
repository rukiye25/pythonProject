a=[[1, 2], [3, 4], [5, 6, 7]]
a=a[::-1]
b=[]
print(a)
for i in a:
    i=i[::-1]
    b.append(i)
print(b)