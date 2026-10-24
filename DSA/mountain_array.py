list = [1,3,4,5,10,11,12,9,8,7,6]

def peak_element(list):
    for i in range(len(list)):
        if(list[i] > list[i+1]):
            print(f"Peak Element is {list[i]}")
            return i

print(peak_element(list))