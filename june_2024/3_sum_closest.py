# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_ = 10000000000
        for i in range(n):
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                sum_ = nums[i]+nums[l]+nums[r] - target
                
                if abs(sum_) <= abs(min_):
                    min_ = sum
                    
                if sum_ == 0:
                    return target
                elif sum_ < 0:
                    l += 1
                else:
                    r -= 1
                    
        return min_ + target
                    

        # mini = 100000000000
        # mt = 10000000000
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
                    
        #             if abs(nums[i] + nums[j] + nums[k] - target) < mt:
        #                 mt = abs(nums[i] + nums[j] + nums[k] - target)
        #                 mini = nums[i] + nums[j] + nums[k]
        #                 print(mini)

        # return mini
        