
mobiles=[
        {"id":1,"name":"samsungs22","brand":"samsung","varients":[
            {"ram":"8gb","rom":"128gb","price":84000},
            {"ram":"8gb","rom":"256gb","price":100000},
        ]},
        {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
            {"ram":"4gb","rom":"128gb","price":54000},
            {"ram":"8gb","rom":"256gb","price":65000},
        ]},
        {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
            {"ram":"8gb","rom":"128gb","price":34000},
            {"ram":"8gb","rom":"256gb","price":45000},
        ]},
            {"id":1,"name":"miii1","brand":"redmi","varients":[
            {"ram":"8gb","rom":"128gb","price":24000},
            {"ram":"8gb","rom":"256gb","price":35000},
        ]},
        ]

# # To print all mobile names

# all_mobile_names=[mob.get("name") for mob in mobiles]

# print(all_mobile_names)

# # To print all brands

# all_brands=[mob.get("brand") for mob in mobiles]

# print(set(all_brands))

# # Price range fron 20k-40k

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(mob.get("name"))

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") < 30000:
#             print(mob.get("name"))            


# price_fliter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]   
# print(price_fliter)         

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

            
# ram_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]

# print(ram_filter)


# 8gb, <40000

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price")<40000 and v.get("ram")=="8gb":
#             print(mob.get("name"))

# print([mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price")<40000 and v.get("ram")=="8gb"])            

#costly mobile

costly_price=max(v.get("price") for mob in mobiles for v in mob.get("varients"))
                 
print(costly_price)
        