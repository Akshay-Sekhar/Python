expenses=[12000,11000,24000,25000,45000,23000,21000]

count=len(expenses)



for i in range(0,count):
    print(expenses[i])

# expenses[1]=15000

print(expenses)

sum=0
for i in range(0,count):
    sum+=expenses[i]
    
print(sum)    