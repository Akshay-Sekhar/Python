text="ABCDABB"

wc={}

for ch in text:
    if ch not in wc:
        wc[ch]=1

    else:
        print(f"first recursive character is {ch}")

        break    