list = []

n = int(input(f"Enter num of elements in the list: "))

for i in range(n):
    num = int(input(f"Element {i+1}: "))
    list.append(num)

print(list)

def linear_search(list):
    Target = int(input(f"Enter a target element to linear serach: "))
    index = 0

    for i in range(n):
        if(list[i] == Target):
            index = i
    return index


print(linear_search(list))

    

