def permuntaion(a,l,r):
    if l==r:
        st=''.join(a)
        print(st)
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permuntaion(a,l+1,r)
            a[l],a[i]=a[i],a[l]
arr="ABC"
lst=list(arr)
n=len(arr)
permuntaion(lst,0,n-1)
