text="Akshay Sekhar is a Mechanical engineering, Graduate from Kerala"

words=text.casefold().replace(",","").split(" ")



wc={}

for w in words:
    if w not in wc:
        wc[w]=1

    else:
        wc[w]+=1

print(wc)            