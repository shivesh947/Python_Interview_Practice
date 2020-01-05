#a4b2c1 convert in aebdcd
# a ->4 bcd e
# b ->2 c d
# c ->1 d
# use unicode a=97 A=65

s="a4b2c1"
n=len(s)
ans=''
for i in range(n):
    if s[i].isalpha():
        ans=ans+s[i]
    else:
        uni=ord(s[i-1]) #ord is used to convert char to unicode
        val=chr(uni+int(s[i]))
        ans=ans+val
print(ans)
