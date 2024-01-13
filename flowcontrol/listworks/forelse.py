lst=[10,11,12,14,15]

num=5

for i in range(0,len(lst)):
    if num==lst[i]:
        print("Element found")
        break

else:
    print("Element not found")