import time #his gives us access to time.time(), which just tells us the current time in seconds.

def timer(func): # Defining function called timer thate takes one input: func, which is another function passed in a value.
    def wrapper(*args, **kwargs): # brand new function called wrapper which runs before and after the function passed. arg and kw are inputs which pass them along.
        start = time.time() # starts time
        result = func(*args, **kwargs) # Function called
        end = time.time() # end time
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def load_page():
    time.sleep(2)   # pretend this is Playwright loading a page
    print("Page loaded")

load_page()

#This actually calls it. Because of @timer, this doesn't just run load_page — it runs wrapper, which:
#Notes the start time
#Runs the real load_page() (which sleeps 2 sec, prints "Page loaded")
#Notes the end time
#Prints how long it took