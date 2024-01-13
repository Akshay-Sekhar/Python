# list=[2,4,5,6]
# count=len(list)

# for i in range(0,count-1):
#     for j in range(i+1,count):
#         if list[i]+list[j]==6:
#             print(f"Numbers are {list[i]} and {list[j]}")
#         elif list[i]+list[j]==7:
#             print(f"Numbers are {list[i]} and {list[j]}")
#         elif list[i]+list[j]==11:
#             print(f"Numbers are {list[i]} and {list[j]}")    
            


arr=[2,3,4,5,6,8]

sum=int(input("Enter sum"))

srt_arr=sorted(arr)

low=0

upp=len(arr)-1

while(low<upp):
    curr_sum=srt_arr[low]+srt_arr[upp]

    if(curr_sum==sum):
        print("Pairs",srt_arr[low],srt_arr[upp])
        low+=1
        upp-=1
    elif(curr_sum>sum):
        upp-=1

    elif(curr_sum<sum):
        low+=1    
