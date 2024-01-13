from re import *

text="abcabABC K@&9"

# pattern="[a-d]"
#  Match either a,b,c ord

# pattern="[a-z]"
#  match a to z

# pattern="[A-Z]"
#  Match A-Z

# pattern="[0-9]"
# pattern="\d"

# pattern="\D"
# exclude digits
# # To check digits

# pattern="[a-zA-Z0-9]"
# pattern="\w"  

# pattern="[^a-z]"
# exclude a-z

# pattern="[^a-zA-Z]"

# pattern="[^a-zA-Z0-9]"
pattern="\W"

matcher=finditer(pattern,text)




# Quandifiers

for m in matcher:
    
    print(m.start(),m.group())
