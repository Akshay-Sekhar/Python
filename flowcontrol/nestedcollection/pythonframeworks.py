frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]


for fw in frameworks:
    if fw.get("language")=="python":
        print(fw.get("name"))

frameworks_name=[fw.get("name") for fw in frameworks if fw.get("language")=="python"]

print(frameworks_name)

frameworks_rating=[fw.get("name") for fw in frameworks if fw.get("rating")==5]

print(frameworks_rating)

id_filter=[fw.get("name") for fw in frameworks if fw.get("id") in range(1,4)]

print(id_filter)