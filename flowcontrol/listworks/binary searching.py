list=[10,2,14,5,6,8,9]

element=int(input("Enter the element"))

list.sort()

low=0
upp=len(list)-1
is_present=False
while(low<=upp):
    mid=(low+upp)//2

    if(element==list[mid]):
        is_present=True
        break

    elif (element>list[mid]):
        low=mid+1

    elif (element<list[mid]):
        upp=mid-1

print(is_present) 
       
