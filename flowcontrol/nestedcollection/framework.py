frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

for fw in frameworks:
    print(fw.get("rating"))

for fw in frameworks:
    print(fw.get("name"))

fw_names=[fw.get("name") for fw in frameworks]
print(fw_names)    

all_rating=[fw.get("rating") for fw in frameworks]
print(all_rating)