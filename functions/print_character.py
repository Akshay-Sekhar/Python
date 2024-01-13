word=input("Enter a word")
count=len(word)
p_str="" 
for i in range(0,count):
    print(word[i])

for i in range(count-1,-1,-1):
    p_str+=word[i]
print(p_str)
print("Palindrome" if p_str==word else "Not palindrome")    