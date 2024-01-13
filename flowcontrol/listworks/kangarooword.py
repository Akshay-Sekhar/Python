source_word=input("Enter source word")
target_word=input("Enter target word")

source_word_lst=[]



for ch in source_word:
    source_word_lst.append(ch)

for ch in target_word:
    char_count=source_word_lst.count(ch)   

    if char_count>0:
        source_word_lst.remove(ch)
       

    else:
        print(f"{target_word} is not kangaroo_word")
        break   
else:

    print(f"{target_word} is a kangaroo_word")         
        