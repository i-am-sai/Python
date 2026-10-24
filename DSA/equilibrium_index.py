list = [-7, 1, 5, 2, -4, 3, 0]
n = len(list)

# Approach 1
def equi_index(list):
    for i in range(n):
        left_sum = 0
        right_sum = 0
        for j in range(0, i+1):
            left_sum = left_sum + list[j]

        for k in range(i+2, n):
            right_sum = right_sum + list[k]
    
        if(left_sum == right_sum):
            print(f"The equi_index is {i+1} and equi_sum is {left_sum}")
            return i+1
        
    return -1


print(equi_index(list))


# Approach 2
def findEquilibrium(arr):
    for i in range(len(arr)):
        # Get left sum
        leftSum = sum(arr[:i])

        # Get right sum
        rightSum = sum(arr[i + 1:])

        # Check the condition
        if leftSum == rightSum:
            return i
    return -1



