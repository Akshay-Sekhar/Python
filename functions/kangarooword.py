source_word=input("Enter the source word")
target_word=input("Enter the target word")
new_word=""
for i in target_word:
    for j in source_word:
        if i==j:
            new_word+=i
print("kangaroo_word" if new_word==target_word else "not a kangaroo word")             

