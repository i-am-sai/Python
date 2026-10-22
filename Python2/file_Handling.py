file = open("data.txt", "r") 
content = file.read()
print(content)
file.close()

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"r+" - Read and Write - Opens a file for both reading and writing, error if the file does not exist

"""
# Above code if error occurs in between file does not close
# with automatically closes the file when the block ends — even if an error occurs inside it.

with open("data.txt", "r") as file:
    content = file.read()
    lines = file.readlines()   # list of lines, each with \n at the end
    print(content)
    for line in file:          # loop line-by-line, memory efficient for big files
        print(line.strip())    # .strip() removes the trailing \n
       
# For large files, looping line-by-line is better — it doesn't load the whole file into memory at once.

with open("data.txt", "w") as file:
    file.write("This is a new\n")
    file.write("file created \n")

with open("data.txt", "a") as file:
    file.write("Another line added\n")

test_results = ["Test 1: Pass", "Test 2: Fail", "Test 3: Pass"]

with open("reports/summary.txt", "w") as file:
   for result in test_results:
       file.write(result + "\n")

import os
if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print(file.read())
else:
    print("File not found")


#Both approaches are valid; checking existence first is more explicit, try/except is more "Pythonic" (Python's general philosophy leans toward "try it and handle failure" over "check first").
try:
    file = open("data.txt")
except FileNotFoundError:
    print("Not Found")
else:
    print("File uploaded")
finally:
    print("Done")