# Validating vehicle number

from re import *

veh_number=input("Enter vehicle number")

# KL-10-AV-0127

pattern="(KL)[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"

matcher=fullmatch(pattern,veh_number)

print("invalid" if matcher==None else "valid")