#90.write a program to merge two array elements
#Input:
#arr1=[10,20,30]
#arr2=[40,50,60]
#output:arr=[10,20,30,40,50,60]
arr1=[10,20,30]
arr2=[40,50,60]
arr1.extend(arr2)
print(arr1)