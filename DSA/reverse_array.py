list = []
n = int(input(f"Enter the number of elements in the list: "))

for i in range(n):
    num = int(input(f"enter {i+1} number: "))
    list.append(num)

print(list)

rev_list = []

for i in range(n):
    num = list[n-i-1]
    rev_list.append(num)

print(rev_list)