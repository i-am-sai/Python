number = int(input("Enter a number: "))

rev_num = 0
while number > 0:
    digit = number % 10
    print(digit)
    rev_num = rev_num * 10 + digit
    number = number//10 

print("Reversed Number is: ", rev_num)





