low=int(input("Enter lower limit"))
upp=int(input("Enter upper limit"))
for year in range(low,upp+1):
    if((year%100==0)and(year%400==0)):
        print(year)
    elif((year%100!=0)and(year%4==0)):
         print(year)   