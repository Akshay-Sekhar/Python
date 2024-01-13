#  Validating gmail id

from re import *

gmail=input("Enter the Gmail id")

pattern="[a-z0-9_.]+@[a-z]{2,}.com" #{2,} => min 2, upper limit not defined

matcher=fullmatch(pattern,gmail)

print("invalid" if matcher==None else "valid")