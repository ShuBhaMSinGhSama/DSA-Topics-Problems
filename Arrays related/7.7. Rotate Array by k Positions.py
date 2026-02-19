a=[3,5,2,6,7,5,8,1,4,8,5,2]
k = 2
k = k % len(a)
arr = arr[-k:] + arr[:-k]
print(arr)
