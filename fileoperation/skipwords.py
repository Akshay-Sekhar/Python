f_news=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\latestnews.txt")

f_stop=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\stopwords.txt")

# for w in f_news:
#     words=w.split(" ")
       

# for w in f_stop:
#     if w not in words:
#     #    word=w
#        print(w)

stop_words={line.rstrip("\n") for line in f_stop}

news_words=set()

for line in f_news:
    words=line.split()
    for w in words:
        news_words.add(w)
print(news_words.difference(stop_words))        




