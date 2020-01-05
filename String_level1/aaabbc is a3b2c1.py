#input="aaabbc"
#output="a3b2c1"
s="aaabbc"
n=len(s)
pre=s[0]
count=1
i=1
ans=''
while i<n:
    if s[i]==pre:
        count=count+1
    else:
        ans=ans+str(count)+pre
        count=1
        pre=s[i]
    if i==n-1:
        ans=ans+str(count)+pre
    i=i+1
    
print(ans)