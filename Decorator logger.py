import datetime
def decorator(decorated_func):
    def wrapper(*args):
        save_result = decorated_func(*args)
        result = "{} - {}\n".format(datetime.datetime.now(),save_result)
        with open('log.txt', 'a') as logger:
            logger.write(result)
        return save_result

    return wrapper





@decorator
def anyfunc(name, age):
    return "Your name is {} and your age is {}.".format(name,age)


print(anyfunc("Max", 25))