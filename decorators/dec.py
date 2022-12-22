# decorator : design pattern in python that allows a user to add new functionality to an existing object without modifying its strucutre.

# called before the definition of a function youwant to decorate

# assigning function to variables

def add_one(number):
    return number+1

result = add_one()
result(5)
print(result)

# # defining functions inside other functions
def plus_one(number):
    def add_one(number):
        return number + 1 
    
    result = add_one(number)
    print(result)
    return result

plus_one(4)

# # passing functions as arguments to other functions
def plus_one(number):
    a = number + 1
    print(a)
    return a 

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

# functions returining other functions
def hello_function():
    def say_hi():
        txt= "HI"
        print(txt)
        return txt
    return say_hi
hello = hello_function()
hello()