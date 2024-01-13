num=int(input("Enter a number"))
sum=0
while(num!=0):
    last_digit=num%10
    sum=sum+last_digit**3
    num=num//10
print(sum)    