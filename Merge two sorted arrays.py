def mergearr(arr1,n,arr2,m):
    arr3=[None]*(n+m)
    i=0
    j=0
    k=0
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            i=i+1
            k=k+1
        else:
            arr3[k]=arr2[j]
            j=j+1
            k=k+1
    
    while i<n:
        arr3[k]=arr1[i]
        i=i+1
        k=k+1
    while j<m:
        arr3[k]=arr2[j]
        j=j+1
        k=k+1
    count=0
    while count<len(arr3):
        print(arr3[count])
        count=count+1
    
arr1=[1,3,5,7,8]
arr2=[2,4,6,9]
n=len(arr1)
m=len(arr2)
mergearr(arr1,n,arr2,m)