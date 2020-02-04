def b_search(list1,val):
    low=0
    high=len(list1)-1
    while low<=high:
        mid=(low+high)//2
        if list1[mid]==val:
            return "found"
        elif val<list1[mid]:
            low=low+1
        else:
            high=high+1
    return "not found"

if __name__ == '__main__': 
	list1 = [1, 11, 12, 15, 19, 90] 
	print ("Given array is", end="\n") 
	key=b_search(list1,999) 
	print(key) 

