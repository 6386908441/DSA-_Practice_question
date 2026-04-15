'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

Each input will have exactly one solution
You cannot use the same element twice
You can return the answer in any order

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

'''
nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
# 2nd method using dictionary
d={}
for i in range(len(nums)):
    diff=target-nums[i]
    if diff in d:
        print(d[diff],i)
    d[nums[i]]=i






