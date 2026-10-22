num_list = []

n = int(input(f"Enter number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    num_list.append(num)
    
def largest_num():
    largest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
    return largest

print(largest_num())

list1=[102,4,1,5,8,2,44,96]

def smallest_num():
    smallest = list1[0]
    for i in list1:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_num())


sorted_list = sorted(list1) #sorted returns a new sorted list from the elements of any iterable. It does not modify the original list.
print(sorted_list)
print(list1) 

# List methods
list1.sort()
print("Smallest number in the list is:", list1[0])
print("Largest number in the list is:", list1[-1])
print("Lenghth of the List is: ", len(list1))
list1.reverse()
print("Reversed List is: ", list1) 
