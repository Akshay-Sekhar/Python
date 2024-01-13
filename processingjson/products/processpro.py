from json import load

path="D:\\Akshay\\C Programing\\July_pythonworks\\processingjson\\products\\items.json"

with open(path,encoding="utf-8") as f:
    data=load(f)

# No of products

# print(len(data)) 

# # all categories
# all_categories={c.get("category") for c in data}

# print(all_categories)

# # electronic products

# electronic_products=[p.get("title")for p in data if p.get("category")=="electronics"]

# print(electronic_products)

# top rated product

top_rated=max(data,key=lambda p:float(p.get("rating").get("rate")))

print(top_rated)


# category women's clothing price range 100-300

women_clothing=[p.get("title") for p in data if p.get("category")=="women's clothing" and p.get("price")>5 and p.get("price")<10]

# women_price=[p.get("title") for p in women_clothing if p.get("price")>5 and p.get("price")<10]

print(women_clothing)

# Jewellery product

jwellery_product=[p.get("title") for p in data if p.get("category")=="jewelery" and p.get("rating").get("rate")]

print(jwellery_product)     

#  Most reviewd product

most_review=max(data, key=lambda p:p.get("rating").get("count"))

print(most_review.get("title"))

# sort wrt price

srt_items=sorted(data,reverse=True, key=lambda p:p.get("price"))

print(srt_items)

# category wise product count

wc={}
for p in data:
    category=p.get("category")
    if category not in wc:
        wc[category]=1 

    else:
        wc[category]+=1

print(wc) 

# max no of category

val_key=[(v,k) for k,v in wc.items()]

print(max(val_key))

print(sorted(val_key))