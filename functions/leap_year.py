def year(n):
    if (n%100==0) and (n%400==0):
        return "leap year"
    elif (n%100!=0) and (n%4==0):
        return "leap year"
    else:
        return "not a leap year" 
    
result = year(2024)
print(result)          