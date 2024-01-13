student={"name":"Akshay","standard":10,"school":"NSS"}


print(student["standard"])

print("name" in student)

if "age" in student:
    print("present")

else:
    print("not present")


student["age"]=15

print(student)

student["name"]="Akshay Sekhar"

print(student)

student["age"]+=2

print(student["age"])