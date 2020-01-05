# input="my name is ram"
# output="ym eman si mar"

s="my name is ram"
# s=input("enter any string")
l=s.split()
l2=[]
for word in l:
	l2.append(word[::-1])
ans=' '.join(l2)
print(ans)