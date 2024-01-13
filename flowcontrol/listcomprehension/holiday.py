lst=[i for i in range(1,8)]

print(lst)

day=["holiday" if day in (1,7) else "workingday" for day in lst]

print(day)