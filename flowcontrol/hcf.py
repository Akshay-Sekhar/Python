num1=int(input("Enter a first number"))
num2=int(input("Enter a second number"))
smallest_number=num1 if num1<num2 else num2   
for i in range(1,smallest_number+1):
    if(num1%i==0)and(num2%i==0):
        hcf=i
print(hcf)