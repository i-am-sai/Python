list = [1,2,3,4,1,2,3,4,4,4,5,6,7,8,9,9,9,9]

target = int(input("Enter the target number to find its frequency: "))


def find_frequency(lst, target):
    count = 0
    for i in lst:
        if i == target:
            count += 1     
    return count
   
print(f"The frequency of {target} is: {find_frequency(list, target)}")

frequency = list.count(target)
print(f"The frequency of {target} is: {frequency}")

number = int(input("Enter a number to check if it has repeated digits: "))
target_digit = int(input("Enter the digit to check its frequency in the number: "))
#12221

def repeated_digit(num):
    digit_count = 0
    while(num > 0):
        digit = num % 10
        if digit == target_digit:
            digit_count += 1
        num = num // 10
    return digit_count

print(f"The digit {target_digit} appears {repeated_digit(number)} times in the number {number}.")