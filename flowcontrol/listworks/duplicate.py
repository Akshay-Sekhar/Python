list1=[25,18,11,21,9]
list2=[21,33,12,9,25]

list1.sort()
list2.sort()

p1=0
p2=0

while(p1<len(list1) and p2<len(list2)):
    if list1[p1]==list2[p2]:
        print("Comman",list1[p1])
        p1+=1
        p2+=1

    elif list1[p1]<list2[p2]:
        p1+=1
    else:
        p2+=1        



