list=[1,2,4,2,6,7,8,3]

i=1


while (i<len(list)-1):

    i+=1

    x=list[i-1]
    y=list[i]
    z=list[i+1]
    
    
    
    if x<y>z:
        
        print("peaks are",x,y,z)

    elif x>y<z:
        
        print("valleys are",x,y,z)

