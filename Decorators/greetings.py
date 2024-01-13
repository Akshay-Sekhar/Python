def capitalize(fn):

    def wrapper():
        
        res=fn()

        res=res.upper()

        return res
    
    return wrapper

@capitalize

def moring_greetings():

    return "good morning"

@capitalize

def evening_greetings():

    return "good evening"

print(moring_greetings())

print(evening_greetings())


from datetime import datetime


@capitalize

def greeting_time():

    current_time=datetime.now()

    current_hour=current_time.hour
    
    if(5<current_hour<12):

        return "Good Morning"

    elif (12<=current_hour<18):

        return "Good Afternoon"

    else:
        return "Good Evening"

def evening_greetings():

    return "good evening"

print(greeting_time())