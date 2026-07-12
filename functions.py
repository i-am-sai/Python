from threading import local


def greet(name):
    message = "Hello, " + name
    return print(message)

greet("Sai")

# greet("Sai") is called, Python creates a new, temporary namespace just for that call — a fresh dictionary-like space 
# to hold name and message. This is called a stack frame. When the function returns, that frame is destroyed and 
# everything inside it (name, message) is gone from memory (unless something outside kept a reference to the returned value).

# Scope: The namespace of a function is called its scope. 
# A variable is only accessible inside the scope it was created in.

x = "global"
print(x) # out of scope, prints global
def outer():
    x = "outer"
    def inner():
        x = "inner" # If I uncomment it prints outer
        print(x)  
    inner() # prints inner
    print(x)
outer() # prints outer
print(x) # out of scope, prints global


count = 10
def incremente():
    global count
    count += 1
    print(count)

incremente() # UnboundLocalError: local variable 'count' referenced before assignment

# Python uses reference counting + garbage collection 
def make_list():
    temp = [1,2,3]
    return temp

my_list= make_list() # my_list now references the list [1,2,3] in memory    
#  temp is gone, but the list object it pointed to survives because my_list now holds a reference to it

