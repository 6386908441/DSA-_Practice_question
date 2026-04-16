'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.

Do not use extra space (O(1) space)
Modify the array in-place
The first k elements should be unique
nums = [1,1,2]
# Expected length = 2
# Expected nums = [1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
# Expected length = 5
# Expected nums = [0,1,2,3,4]
'''
nums = [0,0,1,1,1,2,2,3,3,4]
i=0
for j in range(1,len(nums)):
    if nums[i]!=nums[j]:
        i+=1
        nums[i]=nums[j]
print(i+1)
print(nums[:i+1])