list=[1,2,4,6,8]


limit=len(list)-1
i=0
while(i<limit):
    
    j=i+1
    diff=list[j]-list[i]
    if(diff==1):
        i+=1
    
    else:
        print(list[i]+1,"is the missing number")
        i+=1 
        
        
