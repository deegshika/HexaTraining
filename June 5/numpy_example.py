# 1D Array
import numpy as np

arr=np.array([10,20,30,40,50])

print(arr+5)
print(arr*2)

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

print(arr.shape)

# 2D Array
arr=np.array([
    [10,20,30],
    [40,50,60]
])

print(arr)

arr = np.zeros((3,4))
print(arr)

arr = np.ones((2,3))
print(arr)

arr = np.arange(1, 11)
print(arr)
