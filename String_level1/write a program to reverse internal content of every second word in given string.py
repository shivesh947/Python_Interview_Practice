# input="my name is ram"
# output="my eman is mar"

s="my name is ram"
# s=input("enter any string")
l=s.split()
l2=[]
i=1
for word in l:
	if i%2==0:
		l2.append(word[::-1])
	else:
		l2.append(word)
	i=i+1
ans=' '.join(l2)
print(ans)