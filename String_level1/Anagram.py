s1="care"
s2="race"
n=len(s1)
m=len(s2)
count=0
for i in range(n):
    if n!=m:
        print("No")
        break
    else:
        if s1[i] in s2:
            count=count+1
if count==n:
    print("Yes")
else:
    print("No")

# or in one line
print(sorted(s1)==sorted(s2))