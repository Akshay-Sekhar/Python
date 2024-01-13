text="ABCDABB"

wc={}

for ch in text:
    if ch not in wc:
        wc[ch]=1

    else:
        wc[ch]+=1

print(wc)            