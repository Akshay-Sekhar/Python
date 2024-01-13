cakes=[
    {"id":1,"name":"blueberry","varients":[
        {"shape":"round","size":"1kg","price":600},
        {"shape":"square","size":"2kg","price":1000},
        ]},
    {"id":2,"name":"butterscotch","varients":[
            {"shape":"heart","size":"1kg","price":700},
            {"shape":"round","size":"2kg","price":1200},
        ]},
    {"id":3,"name":"blackforest","varients":[
            {"shape":"square","size":"1kg","price":550},
            {"shape":"heart","size":"2kg","price":900},
        ]},
    ]

# Name of cakes

all_names=[c.get("name") for c in cakes]

print(all_names)

# shape


print([c.get("name") for c in cakes for v in c.get("varients") if v.get("shape")=="round"])


# price less than 1000

print(set([c.get("name") for c in cakes for v in c.get("varients") if v.get("price")<1000]))

# price >550 and size <2kg
print([c.get("name") for c in cakes for v in c.get("varients") if v.get("size")<"2kg" and v.get("price")> 550])

# shape=heart size >1kg

print([c.get("name") for c in cakes for v in c.get("varients") if v.get("shape")=="heart" and v.get("size")>"1kg"])

# price >700, print shape

print([v.get("shape") for c in cakes for v in c.get("varients") if v.get("price")>700])


# print price

print([v.get("price") for c in cakes for v in c.get("varients") if v.get("shape")=="heart"])



