def getMissingNo(a, n): 
    t=(n+1)*(n+2)/2
    for i in range(n):
        t-=arr[i]
    return int(t) 
arr = [1,4,2,3,6] 
print(getMissingNo(arr, len(arr))) 
