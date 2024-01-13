from json import load

path="D:\\Akshay\\C Programing\\July_pythonworks\\processingjson\\country\\data.json"

with open(path,encoding="utf-8") as f:
    data=load(f)

# print(len(data))  

# Regions   

all_regions={r.get("region") for r in data}

# print(all_regions)

# Asian country name

asian_country=[c.get("name") for c in data if c.get("region")=="Asia"]

# print(asian_country)

# Independent country

independent_country=[c.get("name")  for c in data if c.get("independent")==True]

# print(independent_country)

# highest population

pop_country=max(data,key=lambda c:c.get("population"))

print(pop_country.get("name"))

# border sharing with india

india_borders=[c.get("borders") for c in data if c.get("name")=="India"]

print(india_borders)