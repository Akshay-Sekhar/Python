f_read=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\years.txt","r")

f_write=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\leapyears.txt","w")

for line in f_read:
    year=int(line.rstrip("\n"))

    if year%100==0 and year%400==0:
        f_write.write(str(year)+"\n")

    elif year%100!=0 and year%4==0:
        f_write.write(str(year)+"\n")   