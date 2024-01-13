#  Validating aadhar

from re import *

number=input("Enter adhar number")

pattern="\d{4}[\s]?\d{4}[\s]?\d{4}"

matcher=fullmatch(pattern,number)

print("invalid" if matcher==None else "valid")
