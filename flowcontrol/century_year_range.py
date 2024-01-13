low=int(input("Lower limit"))
upp=int(input("Enter upper limit"))
for year in range(low,upp+1):
    if(year%100==0):
        print(year)