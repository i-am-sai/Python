list_num = [2,4,5,6,7,1,8,3]


def even_count(list):
    count = 0
    for num in list_num:
          if(num % 2 == 0):
                count = count + 1
          else:
            continue
    return count


No_even = even_count(list_num)
print(No_even)
