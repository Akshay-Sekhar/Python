list=[10,12,14,11,15]

element=int(input("Enter an element"))

is_present=False
for i in range(0,len(list)):
    if list[i]==element:
        is_present=True
        break
print(is_present)        