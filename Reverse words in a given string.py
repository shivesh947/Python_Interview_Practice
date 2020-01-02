st="hello my name is rahul"
lst=st.split(" ")
print(lst)
lst2=[]
for i in range(len(lst)):
    lst2.insert(0,lst[i])
    
st=' '.join(lst)
print(st)
