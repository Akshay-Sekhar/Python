n1=int(input("Enter num1"))

n2=int(input("Enter num2"))

lst=[10,20,30,40]

loc=int(input("Enter intex position"))

try:
    print(lst[loc])

except Exception as e:
    print(e.args)    

try:
    res=n1/n2

    print(f"result={res}")

except Exception as e:

    print(e.args)

print("Database commit") 

print("File transaction")