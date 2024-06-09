# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0

# Brute Force

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum % k == 0:
                    count += 1
        
        return count

# Optimal

class Solution1:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        m = {0:1}
        s = 0
        for i in nums:
            s += i
            mod = s % k
            count += m.get(mod, 0)
            m[mod] = m.get(mod, 0) + 1
        return count


        
