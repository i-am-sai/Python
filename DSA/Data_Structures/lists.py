# In Python lists are built in data structures that serves as dynamic array
# It is ordered, mutable and contain elements of different data types.

list = [1,2,"one","two"]
list1 = [102,4,1,5,8,2,44,96]

#python lists come with several built in algorithms(called methods) to perform common operations like appending, sorting and more
print(sorted(list1))
list.append(3)
print(list)
print(list1)
print(list1.sort())
#This design is intentional in Python. Methods that mutate an object (like sort(), append(), extend(), reverse(), clear()) typically return None to make it clear that they modify the object rather than produce a new one.
list1.sort()
print(len(list1))


#Algorithms: Sometimes we want to perform actions that are not built into Python.
# Prob1:The lowest value in a list
list2=[102,4,1,5,8,2,44,96]

min_Var = list2[0]

for i in list2:
    if i < min_Var:
        min_Var = i
print("Lowest Value:", min_Var)

merged = list1 + list2
print(merged)
print(len(merged))

