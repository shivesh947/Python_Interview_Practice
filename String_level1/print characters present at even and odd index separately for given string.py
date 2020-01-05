#s="RAHUL"
#   01234
#output
#R H L
#A U
s="Rahul"
print(s[::2])
print(s[1::2])


#or

i=0
print("even index")
while i<len(s):
	print(s[i])
	i=i+2
	
i=1
print("odd index")
while i<len(s):
	print(s[i])
	i=i+2