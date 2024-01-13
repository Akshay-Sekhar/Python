text="ABACCD"

lst=[]

for ch in text:
    char_count=lst.count(ch)

    if char_count==0:
        lst.append(ch)

    else:
        print(f"First recursive character is {ch}")  
        break  


