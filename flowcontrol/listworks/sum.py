expenses=[12000,11000,24000,25000,45000,23000,21000]

# count=len(expenses)

# sum=0

# for i in range(0,count):
#     sum+=expenses[i]

# print(sum)      



total=sum(expenses)
print(total)

lg_expenses=max(expenses)
print(lg_expenses)

sm_expenses=min(expenses)
print(sm_expenses)

reverse_sort=sorted(expenses,reverse=True)
print(reverse_sort)