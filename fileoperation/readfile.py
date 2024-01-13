# To read the file data.txt

f=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\data.txt","r")

# for line in f:
#     print(line)

words=[line.rstrip("\n") for line in f]

print(words)

f.close()    