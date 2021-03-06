import datetime


def choose_action(action):
    text = "Looking for action..."

    if action == "hello":
        text = hello()
    elif action == "time":
        text = get_time()
    elif action == "date":
        text = get_date()
    elif action == "herokupassword":
        text = get_herokupassword()
    elif action == "githubpassword":
        text = get_githubpassword()
    elif action == "dialogflowpassword":
        text = get_dialogflowpassword()
    elif action == "name"
        text = get_name()
    else:
        text = "No action matched!"

    return text



def hello():
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello World"
    return text


def get_time():
    """
    Tells the user the current time
    """
    print('time action')

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    text = "The time is %d:%d" % (hour, minute)
    return text

def get_date():
    """
    Tells the user the current date
    """
    print('date action')

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    text = "The date is %d-%d-%d" % (month, day, year)
    return text


def get_herokupassword():
    """
    Tells the user their heroku password
    """
    print('herokupassword action')
    password = "justeatfood"
    return password
    
def get_githubpassword():
    """
    Tells the user their github password
    """
    print('githubpassword action')
    password = "foodislove"
    return password
def get_dialogflowpassword():
    """
    Tells the user their dialog flow password
    """
    print('dialogflowpassword action')
    password = "ilovefood"
    return password
def get_name():
    """
    Tells the user their name
    """
    print('name action')
    name = Jay
    return name
    
