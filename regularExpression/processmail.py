from re import *

f=open("D:\\Akshay\\C Programing\\July_pythonworks\\regularExpression\\mails.txt")

pattern="[a-z0-9_.]+@[a-z]{2,}.com"

for line in f:
    mail=line.rstrip("\n")
    matcher=fullmatch(pattern,mail)

    if matcher!=None:

        print(mail)