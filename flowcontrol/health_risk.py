gender="women"
tummy_size=95
buttock_size=75
value=tummy_size/buttock_size
if(gender=="women"): 
    if(value<=0.80):
        print("Health risk is low")
    elif((value>=0.81)and(value<=0.85)):  
        print("Health risk is moderate")  
    else:
        print("Health risk is high")  
if(gender=="male"):
    if(value<=0.95):
         print("Health risk is low")
    elif((value>=0.96) and (value<=1)):
        print("Health risk is moderate")
    else:
         print("Health risk is high")    

