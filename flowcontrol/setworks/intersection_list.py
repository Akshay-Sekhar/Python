lst1=[10,11,12,13,14]
lst2=[11,15,13,14,16]

st_lst1=set(lst1)
st_lst2=set(lst2)

common_elements=st_lst1.intersection(st_lst2)

print(common_elements)