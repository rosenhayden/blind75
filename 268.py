# first intuition is sorting and doing a pass making sure |nums[i] - (nums[i+1])| is always 1 when its not, return nums[i]+1. time nlogn +n from sorting plus one pass




# there is probably an o(n) way.
# there is: sum for i=0 to i = len i+=1, this is the actual totatl sum. now compute nums totatl sum. The difference is the missing number.
# [3,0,1]
# 1+ 2 + 3 = 6 vs 3 + 0 + 1 =4 diff = 2
# big example 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45 vs 37 diff = 8 thats solution

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        target, actual = 0, 0
        for i in range(1,len(nums)+1):
            target += i
            actual += nums[i-1]
        return target - actual

""" Old jank naive
        nums.sort()
        print(len(nums))
        if len(nums) == 1 :
            if nums[0] == 0:
                return 1
            else:
                return 0
        if nums[0] != 0:
            return 0
        for i in range(len(nums)-1):
            print(nums[i])
            print(nums[i+1])
            if nums[i+1] - nums[i] != 1:
                return nums[i]+1
        return nums[len(nums)-1] + 1
"""
