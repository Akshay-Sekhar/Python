# starting with an alphabe k,l,m,n 
# second must be a digit divisible by 3
# followed by any no of alphabets and digits

from re import *

var_name=input("Enter a variable name")

pattern="[k-n][369][a-zA-Z0-9]+"

matcher=fullmatch(pattern,var_name)

print("invalid" if matcher==None else "valid")