def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums


print(selection_sort([5, 7, 8, 4, 1, 6, 9, 2]))