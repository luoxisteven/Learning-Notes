def bubble_sort(num_list):
    for a in range(len(num_list) - 1):
        for b in range(len(num_list) - a - 1):
            if num_list[b] > num_list[b+1]:
                num_list[b], num_list[b+1] = num_list[b+1], num_list[b]
    return num_list

def selection_sort(num_list):
    for a in range(len(num_list) - 1):
        min_num = num_list[a]
        idx = a
        for b in range(a + 1, len(num_list)):
            if num_list[b] < min_num:
                min_num = num_list[b]
                idx = b
        num_list[a], num_list[idx] = num_list[idx], num_list[a]
    return num_list

def insertion_sort(num_list):
    for a in range(1, len(num_list)):
        for b in range(a, 0, -1):
            if num_list[b] < num_list[b-1]:
                num_list[b], num_list[b-1] = num_list[b-1], num_list[b]
            else:
                break
    return num_list

def merge_sort(num_list):
    def conquer(num_list1, num_list2):
        left = 0
        right = 0
        num_list = []
        while left < len(num_list1) and right < len(num_list2):
            if num_list1[left] <= num_list2[right]:
                num_list.append(num_list1[left])
                left += 1
            else:
                num_list.append(num_list2[right])
                right += 1
        if left < len(num_list1):
            num_list += num_list1[left:]
        if right < len(num_list2):
            num_list += num_list2[right:]
        return num_list
    
    def divide(num_list):
        if len(num_list) == 1:
            return num_list
        else:
            return conquer(divide(num_list[:len(num_list)//2]), divide(num_list[len(num_list)//2: len(num_list)]))
        
    return divide(num_list)

nums = [1,12,-5,-6,50,3]
print(merge_sort(nums))