print("Python is working")

# Data Types
age = 23   # int: whole numbers
version = 7.7 # float: decimal numbers
name = "Sai"  # string: text 
is_ready = True  # boolean : True or False

# Checking the type: type(): This is useful when debugging dynamic code.
print(type(age))
print(type(version))
print(type(name))
print(type(is_ready))

# Multiple assignment
x = y = z = 0 # all three get value 0
host, port = "localhost", 8080 # 2 variables in one line

print(x, y, z)

# String Operations: More flexible than java
host = "akami"
domain = ".com"

full = host + domain #Concatenation
print(full)
print(len(full)) #length of the strings (space is also counted in char length)

#Repetition
line = ("7" " " )*20
print(line)

# f-string (most modern way - like String.format in Java): formatted string literals
#Interpolation: Variables are embedded directly.
ip = "192.160.1.1"
port = 22
print(f"Connecting to {ip} on port {port}")

#Uppercase / Lowercase
print(host.upper())
print(host.lower())

# Type Conversion
port ="8080"    # This is a string
port = int(port) # Now it's a int

number = 42
text = str(number) # int to string
price = int(3.99) # float to a int (Truncates, doesn't round)
print(price)
print(price + price)

Name  = "Sai"
Age = "23"
Role = "QA Automation"
Learning_Python = True

print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"Current Role: {Role}")
print(f"Role has {len(Role)} characters")

#Arithmetic Operators
a = 10
b = 3
print(a + b, a -b, a*b, a/b, a//b, a%b, a**b)

#Comparission Operators
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

#Logical Operators (Python uses plain English words instead of symbols. Much more readable)
#Java =    &&, ||, !
#Python = and, or, not

is_connected = True
has_error = False
print(is_connected and has_error)
print(is_connected or has_error)
print(not is_connected)

# User Input: input() always returns as string
name = input("Enter your name: ")
print(f"Hello {name}")

port = input("Enter port number: ")
print(type(port))

port = int(input("Enter port number: "))
print(type(port))

age = int(input("Enter age"))

# Conditionals
if (age>18):   #No parentheses around condition (optional but not needed)
    print("Adult")
elif age==18:
    print("Teen")
else:
    print("Minor")