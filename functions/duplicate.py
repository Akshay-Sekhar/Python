# word="Good Morning"
# for ch in word:
#     count=word.count(ch)
#     if count>1:
#         print(ch)



word="Good Morning"
srt_word=sorted(word)
count=len(word)

for i in range(0,count-1):
    j=i+1
    if(srt_word[i]==srt_word[j]):
        print(srt_word[i])
