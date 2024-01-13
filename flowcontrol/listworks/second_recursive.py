text="ABACCD"

lst=[]

for ch in text:
    char_count=lst.count(ch)

    if char_count==0:
        lst.append(ch)

    else:
        recursive_ch=ch
print(f"Second recursive character is {recursive_ch}")


# or

text="ABACDC"

lst=[]

dup_lst=[]

for ch in text:
    char_count=lst.count(ch)

    if char_count==0:
        lst.append(ch)

    else:
        dup_lst.append(ch)

print(f"second recursive character is {dup_lst[1]}")        

