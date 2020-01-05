# input="3A1CB2"
# ouput="ABC123"

s="3A1CB2"
alpha=[]
num=[]
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num.append(ch)
s=''.join(sorted(alpha)+sorted(num))
print(s)