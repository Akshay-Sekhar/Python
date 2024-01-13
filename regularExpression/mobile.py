# validate mobile number

from re import *

mob=input("Enter a mobile number")

Pattern="\d{3}[-]?\d{3}[-]?\d{4}"

matcher=fullmatch(Pattern,mob)

print("invalid" if matcher==None else "valid")