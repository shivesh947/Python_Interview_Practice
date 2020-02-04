def pivotplace(list1,first,last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
             left=left+1
        while left<=right and list1[right]>=pivot:
             right=right-1
        if right<left:
             break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right

def quickSort(list1,first,last):
    if first<last:
        p=pivotplace(list1,first,last)
        pivotplace(list1,first,p-1)
        pivotplace(list1,p+1,last)

def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i],end=" ") 
	print() 

if __name__ == '__main__': 
	list1 = [12, 11, 13, 5, 6, 7] 
	print ("Given array is", end="\n") 
	printList(list1) 
	quickSort(list1,0,len(list1)-1) 
	print("Sorted array is: ", end="\n") 
	printList(list1) 

