all_users=["mammootty","mohanlal","prithvi","dq","fahad","nivin"]

nivin_friends=["asif","dq","fahad"]

dq_friends=["mammootty","mohanla","fahad","asif"]

all_users_set=set(all_users)

nivin_friends_set=set(nivin_friends)

suggestions=all_users_set.difference(nivin_friends_set)

suggestions.discard("nivin")

print(suggestions)

mutual_friends=nivin_friends_set.intersection(dq_friends)

print(mutual_friends)





