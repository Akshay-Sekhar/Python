text="I have 1 car 2 bikes and 3 cycles"
words=text.split(" ")
print(words)
for w in words:
    if w.isdigit():
        print(w)