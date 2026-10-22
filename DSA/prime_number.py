number = int(input("Enter a number: "))

if(number < 2):
    print(f"{number} * is a prime number")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if(number % i == 0):
            print(f"{number} * is not a prime number")
            break
    else:
        print(f"{number} * is a prime number")
            

def is_prime(num):
    flag = 0
    if(num == 0 or num == 1):
        return False
    else:
        for i in range(2, num//2 + 1): # To check the divisors of the number, we only need to check up to num//2
            if(num % i == 0):
                print(f"{num} is not a prime number")
                flag = 1
                break
        if(flag == 0):
            print(f"{num} is a prime number")
            return True

is_prime(number)
