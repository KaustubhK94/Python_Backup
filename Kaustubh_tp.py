def total_list(list_k):
    total = 0
    for item in list_k:
        total = item + total
    return total

my_list = [1,2,3,4,5,6,7]

total_list(my_list)
