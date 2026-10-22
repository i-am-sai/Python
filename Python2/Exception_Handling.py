


try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Invalid input. Please enter a valid age.")

#Catching specific errors vs. any error
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero.")

#Catching multiple specific errors
try:
    num = int(input("Enter a number: "))
    result = 10/num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

try:
    value =int("abc")
except ValueError:
    print("Invalid conversion")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Catch anything generically by exception (use sparingly as it hides the real problem if overused)

# def risky_code():
#     return print(7)

try:
    risky_code()
except Exception as e:
    print(f"Something went wrong: {e}")

# as e capturese the actual error object, so you can inspect what happened rather than just knowing something failed.

# else and finally blocks: else runs if no exception, finally always runs regardless of exception

try: 
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
finally:
    print("Execution completed.")
# else: block executes only when try block succeded with zero errors
# finally: runs always, whether there was an error or not. Used for cleanup: closing files, closing browser session and releasing resources.

# Raising your own exceptions:

def set_age(age):
    print(f"Age set to {age}")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
    return age

set_age(-5)