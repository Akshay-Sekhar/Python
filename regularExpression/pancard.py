# Validate pan card number

from re import *

pan=input("Enter pan number")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}?"

matcher=fullmatch(pattern,pan)

print("invalid" if matcher==None else "valid")