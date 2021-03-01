list=[]
table=1
for i in range(10):
    list.append([])
    for j in range(1,11):
        list[i].append(table*j)
    table=2+i
print(list)