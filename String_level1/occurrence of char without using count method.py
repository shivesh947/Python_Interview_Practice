s="abacabb"
ouc={} # use set
for i in range(len(s)):
    ouc[s[i]]=ouc.get(s[i],0)+1 #get(find,0) get methode is use to find key present or not if not return 0
print(ouc)