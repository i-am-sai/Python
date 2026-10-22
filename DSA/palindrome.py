number = int(input("Enter a number to check if it is a palindrome or not: "))

def is_palindrome(num):
    original_num = num
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num//10
    
    if original_num == rev_num:
        return True
    else:
        return False

print(is_palindrome(number))
