mobile={"name":"Samsung","processor":"Exynos","price":15000}

print(mobile["name"])

if "price" in mobile:
    print(mobile["price"])

else:
    print("Invalid Key")

mobile["offer"]=2000


mobile["price"]-=2000

print(mobile)

