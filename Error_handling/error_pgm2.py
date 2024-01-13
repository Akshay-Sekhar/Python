n1=int(input("Enter num1"))
n2=int(input("Emter num2"))

try:
    res=n1/n2

    print(f"Result is {res}")

except Exception as e:

    n2=int(input("Enetr another value for n2"))

    res=n1/n2

    print(f"Result is {res}")

finally:

    print("Database commit")

    print("File transaction")        