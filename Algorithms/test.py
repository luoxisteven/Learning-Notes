def quick_sort(num_list):
    if len(num_list) == 0:
        return []
    pivot_num = num_list[len(num_list)//2]
    larger = []
    smaller = []
    pivot = []
    for num in num_list:
        if num > pivot_num:
            larger.append(num)
        elif num < pivot_num:
            smaller.append(num)
        else:
            pivot.append(num)
    return quick_sort(smaller) + pivot + quick_sort(larger)

print(quick_sort([2,3,6,3,23,234]))

