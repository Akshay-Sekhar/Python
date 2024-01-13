lst=[1,2,3,4,5,6]

max_num=lst[-1]
# max_num=max(lst)

total_sum=max_num*(max_num+1)//2

cur_sum=sum(lst)

diff=total_sum-cur_sum

if(diff==0):
    print(max_num+1, "is the missing number")

else:
    print(diff, "is the missing number")    



 