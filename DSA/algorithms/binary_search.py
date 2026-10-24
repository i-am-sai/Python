list = [1,3,4,6,7,9,10,24]
# Buuble sort wil only apply for sorted array

def binary_search(list, target):
    start = 0
    end = len(list) - 1

    while(end >= start):
        mid = (start + end) // 2

        if(list[mid] == target):
            return mid
        
        elif(list[mid] < target):
            start = mid + 1
        
        elif(list[mid] > target):
            end = mid - 1
            
    return -1

print(binary_search(list, 6))





