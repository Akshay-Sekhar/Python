f=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\news.txt","r")
wc={}
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1

print(wc)             