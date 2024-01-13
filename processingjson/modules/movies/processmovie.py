from json import load

path="D:\\Akshay\\C Programing\\July_pythonworks\\processingjson\\modules\\movies\\db.json"

with open(path) as f:

    data=load(f)

# print(len(data)) 

# #  print movie names

# all_names=[t.get("Title") for t in data]

# print(all_names)

# # print all directors

# all_directors={m.get("Director") for m in data}
# # set is used to avoid duplicates

# all_directors.discard("N/A")

# print(all_directors)
 
# # highest imdb rating

# filtered_data=[m for m in data if m.get("imdbRating")!="N/A"]

# top_movie=max(filtered_data, key=lambda m: float(m.get("imdbRating")))

# print(top_movie.get("Title"))

#  Genre

# all_genre=set ()
# for m in data:
#     for g in m.get("Genre").split():
#         all_genre.add(g.rstrip(","))
# print(all_genre)

# Action

# for m in data:
#     if m.get("Genre").count("Action")>0:
#         print(m.get("Title"))

# Movie  after 2014
for m in data:
    released_date=m.get("Released")
    year=released_date.split(" ")[-1] 

if year.isdigit():
    if int(year)>2014:
        print(m.get("Title"))    


