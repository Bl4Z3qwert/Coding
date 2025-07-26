import numpy as np
arr=np.array([1,2,3,6,5,7,4,8,2,9,6,4,5,8,])
print(arr)
print(arr.dtype)
print(type(arr))
print(arr[2])


print(arr[1:7:3])


ar=np.array([1,3,6,6,7], dtype='S')
print(ar)
print(ar.dtype)



arry=np.array([[1,2,3,4,5] , [5,6,7,8,9]])
print(arry[1,3])
print(arry.shape)

ary=np.array([1,2,3,4,5,6,7,8,910,11,12])
new=ary.reshape(3,4)
print(new)
for x in arr:
    print(x)
    