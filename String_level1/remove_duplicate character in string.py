#input="aaabbbdddccce"
#output="abcde"
s="aaabbbdddccce"
n=len(s)
ans=''
for i in range(n):
    if s[i] not in ans:
        ans=ans+s[i]
print(ans)
print(''.join(sorted(ans)))

#or use set
print(''.join(set(s)))