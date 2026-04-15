# write program reverse array using recursion function
def reverse_array(nums, left, right):
    if left >= right:
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    return reverse_array(nums, left + 1, right - 1)


list1 = reverse_array([1, 5, 6, 7, 8, 9], 2, 4)
print(list1)
