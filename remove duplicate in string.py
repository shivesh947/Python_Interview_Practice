def removedub(lt,n):
    hmp=[]
    for i in range(n):
        if lt[i] in hmp: 
            continue
        else:
            hmp.append(lt[i])
    print(''.join(hmp))
n=input()
for i in range(int(n)):
    arr=input()
    removedub(str(arr),len(arr))
    