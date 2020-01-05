s="aaabcabbbccd"
lst=[]
for i in range(len(s)):
    if s[i] not in lst:
        lst.append(s[i])
for i in range(len(lst)):
    print(lst[i]+" =",s.count(lst[i]))

