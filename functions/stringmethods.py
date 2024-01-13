# casefold
name="LuminaR TechnoLab"
print(name.casefold())

# Capitalize
name="luminar technolab"
print(name.capitalize())


# count
name="Luminar Technolab"
print(name.count("a"))


# startswith
name="Luminar Technolab"
print(name.startswith("hu"))


# endswith
name="Luminar Technolab"
print(name.endswith("lab"))
print(name.endswith("Lab"))


# count case insesitive
name="Luminar Technolab"
print(name.casefold().count("l"))


#isalpha            Space considered  
name="Luminar Technolab"  
print(name.isalpha())

name="Luminartechnolab"
print(name.isalpha())



# isdigit
name="1234"
print(name.isdigit())

name="1234 hello"
print(name.isdigit())



name="luminartechnolab123"
print(name.isalnum())
name="Luminar technolab 123"
print(name.isalnum())



name="Hello Good Morning All"
words=name.split(" ")
print(words)
for w in words:
    print(w)

name="Hello,Good,Morning,All"
words=name.split(",")
print(words)
for w in words:
    print(w)
