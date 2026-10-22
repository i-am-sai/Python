# Fibonacci series : 0,1,1,2,3,5,8,13;

num = int(input(f"Enter the number of terms for Fibonacci series: "))

a = 0
b = 1
count = 2
list = [0, 1]

while(count < num):
    temp = b
    b = a + b
    a = temp
    count += 1
    list.append(b)

print(f"Fibonacci series for {num} terms is: {list}")


def fibonacci(n):
    if n <= 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    else:
        fib_series = [0,1]
        for i in range(2,n):
            next_term = fib_series[i-1] + fib_series[i-2]
            fib_series.append(next_term)
        return fib_series

print(f"Fib series: {fibonacci(num)}")
