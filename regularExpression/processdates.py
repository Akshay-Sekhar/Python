from re import *

f=open("D:\\Akshay\\C Programing\\July_pythonworks\\regularExpression\\dates.txt")

# pattern="\d{4}[-/]\d{2}[-/]\d{2}"

pattern="(20)([01][0-9]|2[0-3])[-/](0[1-9]|1[0-2])[-/]([0][1-9]|[12][0-9]|[3][0-1])" # Dates 20th century

for line in f:

    date=line.rstrip("\n")

    matcher=fullmatch(pattern,date)

    if matcher!=None:

        print(date)


