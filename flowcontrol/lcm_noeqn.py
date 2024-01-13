num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
largest_number=num1 if num1>num2 else num2
product=num1*num2
lcm=1
for i in range(largest_number,product+1):
    if(i%num1==0)and(i%num2==0):
        lcm=i
        break
print(lcm)    