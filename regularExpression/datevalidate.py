#  Validating a date

from re import *

date=input("Enter date")

Pattern="\d{4}[-]\d{2}[-]\d{2}"

matcher=fullmatch(Pattern,date)

print("invalid" if matcher==None else "valid")