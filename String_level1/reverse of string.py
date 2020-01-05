#using slice operater-------------------------------------->
s="hello"

print("using slice operater = "+(s[::-1])) 
#s[begin:eng:steps] 
# steps never 0 if 0 its show error, 
# if step + ->
# if strp - <-

#using reverse--------------------------------------------->

r=reversed(s)  #reversed function return array of reverse of string cannot be direct print
rv=''.join(r)
print("using reverse function = "+rv) 

#without using pre-define function ------------------------->
i=len(s)-1
d=""
while i>=0:
	d=d+s[i]
	i=i-1
print("without using function = "+d)
