num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

smallest_number=num1 if num1<num2 else num2
for i in range(1,smallest_number+1):
    if(num1%i==0) and (num2%i==0):
        gcd=i
lcm=(num1*num2)/gcd
print(lcm)