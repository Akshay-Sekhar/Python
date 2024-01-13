f1=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\allstudents.txt","r")

f2=open("D:\\Akshay\\C Programing\\July_pythonworks\\fileoperation\\failed.txt","r")

all_students={line.rstrip("\n") for line in f1}

failed_studemts={line.rstrip("\n") for line in f2}

passed_students=all_students.difference(failed_studemts)

print(passed_students)