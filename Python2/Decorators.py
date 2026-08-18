#DECORATORTS:

#Prereq: Functions are objects too
def wish():
    return "hello"

say_hello = wish #no parenthesis, this copies the reference object, doesn't call it
print(say_hello()) # prints hello
# Notice wish without () refers to the function object itself. wis() calls it. This distinction is everything for decorators.

# A function that takes a function and returns a function

def shout(func):
    def wrapper():
        result = func() # call the original function
        return result.upper() # modify the result
    return wrapper # return the wrapper function

def greet():
    return "Hello!"

loud_greet = shout(greet)
print(loud_greet()) # prints "HELLO!"

# A functin wrapping another function to add behaviour without changing its code is a decorator.
@shout
def greet1():
    return "hello"
# @shout = loud_greet = shout(greet) 100% equivalent to the above, but more elegant and readable. The @ symbol is syntactic sugar for decorators.   
print(greet1())   # "HELLO" 