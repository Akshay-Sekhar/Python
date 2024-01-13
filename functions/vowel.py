word="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels="a","e","i","o","u"
v_count=0
c_count=0
for ch in word:
    if ch in vowels:
        v_count+=1
    elif ch.isalpha:
        c_count+=1 
print(f"Total number of characters is {len(word)}")        
print(f"Number of vowels is {v_count}")
print(f"Number of vowels is {c_count}")          
