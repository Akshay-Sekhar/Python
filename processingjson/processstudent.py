from json import load

# f=open("D:\Akshay\C Programing\July_pythonworks\processingjson\students.json")

# data=load(f)

# # no of students

# print(len(data))

# # name of students

# all_names=[st.get("name") for st in data]

# print(all_names)

path="D:\Akshay\C Programing\July_pythonworks\processingjson\students.json"

with open(path) as f:

    data=load(f)

print(len(data))    