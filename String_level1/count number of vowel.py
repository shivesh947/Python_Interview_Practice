s="progRAMING"
d1={'a','e','i','o','u','A','E','I','O','U'}
d2={}
for ch in s:
    if ch in d1:
        d2[ch]=d2.get(ch,0)+1

for i in sorted(d2.items()):
    print(i,d2.get(i))

    