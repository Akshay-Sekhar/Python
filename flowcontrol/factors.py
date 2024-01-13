num1=int(input("Enter a first number"))
num2=int(input("Enter a second number"))
if(num1>num2):
    smallest_num=num2
else:
    smallest_num=num1    
for i in range(2,smallest_num+1):
    if(num1%i==0)and(num2%i==0):
        print(i)
