arr1=["cat","bat","rat"]
arr2=["hat","rat","sweet","bat"]
res = []
for i in arr1 :
    for j in arr2:
        if (i==j):
            res.append(j)
            
            print (res)
