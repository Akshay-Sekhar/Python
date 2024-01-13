f_read=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\vehiclenos.txt")

f_write=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\keralavehiclenos.txt","w")

for line in f_read:
    reg_number=line.rstrip("\n")

    if reg_number.startswith("kl"):
        f_write.write(reg_number+"\n")