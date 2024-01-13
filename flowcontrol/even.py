low=int(input("Lower limit"))
upp=int(input("Upper limit"))
for num in range(low,upp+1):
    if(num%2==0):
        print(num)