# Multiplication

def product(*args):
    res=1
    for n in args:
        res*=n
    return res

print(product(10,20))

print(product(1,2,3,4,5,6,7,8,9))

def adder(*args):
    return sum(args)

print(adder(10,20))


def concat_string(*args):

    return " ".join(args)

print(concat_string("hello","good morning","have","a","nice","day"))   

def reverse_concat(*args):
    data=list(args)
    data.reverse()

    return " ".join(data)

print(reverse_concat("red","green","blue"))


# Key word arguments

def person_name(**kwargs):
    print(kwargs)

person_name(first_name="sachin",second_nem="ramesh",third_name="tendulkar")


# o/p john has 2 year experience in web development

def emp_details(**kwargs):
    name=kwargs.get("name")
    exp=kwargs.get("exp")
    dept=kwargs.get("dept")

    print(f"{name} has {exp} experience in {dept}")

emp_details(name="john",exp="2 year", dept="web development")


def balance_enq(**kwargs):
    bank_name=kwargs.get("bank_name")

    acno=kwargs.get("acno")

    balance=kwargs.get("balance")

    print(f"your {bank_name} {acno} account bal is INR {balance}")

balance_enq(bank_name="sbi",acno="12334",balance="23455") 


# Both args and kwargs

def perform_operation(*args,**kwargs):

    num1,num2=args

    op=kwargs.get("operand")

    if op=="+":
        return num1+num2
    
    elif op=="-":
        return num1-num2
    
    elif op=="*":
        return num1*num2
    
    elif op=="/":
        return num1/num2
    
    else:
        return "invalid operand"
    
print(perform_operation(10,20,operand="*"))    

