def subArraySum(arr, n, sum): 
    curr_sum=arr[0]
    start=0
    i=1
    while i<=n:
        while curr_sum>sum and start<i-1:
            curr_sum=curr_sum-arr[start]
            start=start+1
            print(arr[start-1])
        if curr_sum==sum:
            print ("%d and %d"%(start, i-1)) 
            return 1
        if curr_sum<sum:
            curr_sum=curr_sum+arr[i]
        i=i+1
    return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 33

subArraySum(arr, n, sum) 

