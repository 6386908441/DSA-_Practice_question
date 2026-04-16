'''
Given an integer array nums and an integer val, remove all occurrences of val in-place and return the new length.

Do not allocate extra space
Modify the array in-place
Order of elements can be changed
First k elements should not contain val
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
Modified array: [0,1,3,0,4,_,_,_]
'''


nums = [0,1,2,2,3,0,4,2]; val = 2


i = 0
for j in range(len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1

print(i)        # new length
print(nums[:i]) # modified array