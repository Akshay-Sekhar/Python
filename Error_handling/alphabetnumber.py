val=input("Enter the value")

if val.isalnum()==False:

    raise Exception("Only numbers and alphabet allowed")

else:
    print("Test pass")