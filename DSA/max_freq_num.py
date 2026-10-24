list = [1,4,2,1,1,2,4,4,4,1,3,4,4,4,2,2,2,2,2]
n = len(list)

def max_freq_num(list):
    count1 = 0
    count2 = 0
    max_num = list[0]
    for i in range(n):
        count1 = 0
        for j in range (n):
            if(list[i] == list[j]):
                count1 += 1
        if(count1 > count2):
            count2 = count1
            max_num = list[i]
    print(f"max freq number is: {max_num} and count is {count2}")
    return count2

print(max_freq_num(list))
        

# Another approach (edge case): what if 2 numbers with same frequency
# Concept: dictionary, handles ties and list comprehension

counts = {} # empty dictionary
for num in list: # visit each value in list
    counts[num] = counts.get(num, 0) + 1

# result: counts = {1:4, 4:7, 2:7, 3:1}

max_count = max(counts.values()) # 7
most_frequent = [
    num for num, count in counts.items()
    if count == max_count
]

print(f"Most frequent number(s): {most_frequent}")
print(f"Frequency: {max_count}")