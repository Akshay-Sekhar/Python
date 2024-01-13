val=input("Enter the number")


if val.isdigit()==False:
    
    raise Exception("Only integers allowed")

else:
    print("Test pass")