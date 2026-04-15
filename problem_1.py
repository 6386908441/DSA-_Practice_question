'''Problem Statement:
Given an integer array nums, return true if any value appears at least twice,
and return false if every element is distinct.

🔹 Example
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


# 1st method(optimal and time complexity O(n) and space complexity o(n)
def check_duplicates(nums):
    feq = {}
    flag = False
    for num in nums:
        if num in feq:
            feq[num] += 1
            flag = True
        else:
            feq[num] = 1

    return flag


print(check_duplicates([1, 2, 3, 1, 4]))


#2nd method using sorting  time complexity o(n2)
def check_duplicates2(nums):
    l = sorted(nums)
    flag = False
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                flag = True

    return flag


print(check_duplicates2([1,2,3,4,1]))
# 3rd method
def check_duplicates3(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


print(check_duplicates3([1,2,3,4,1]))
