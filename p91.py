#91.write a program to print non repeated array elements
#Input: arr1=[1,2,3,1,5]
#output:Non Repeated array elements are :2,3,5
arr1=[1,2,3,1,5]
arr2=[1,2,3,1,6]
res= []
for i in arr1 :
    for j in arr2:
        if (i==j):
            res.remove(i)
            
print (res)