from re import *

text="abaabcaabaaaa"

# pattern="a+" #  Atleast one a 

# pattern="a*" # any no of a including 0

# pattern="a?" # optional

# pattern="a{2}" # occurance of 2 a

pattern="a{2,3}" # a min 2 and max 3

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())