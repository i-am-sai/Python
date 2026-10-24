list = [5,6,8,1,3,0,2,7]
n = len(list) - 1

def bubble_sort(list):

    for i in range(n):
        for j in range(1, n-i):
            if(list[j-1] > list[j]):
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
    return list

print(list)
print(bubble_sort(list))
