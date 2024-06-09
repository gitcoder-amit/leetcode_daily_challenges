# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false


# Brute Force
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
            if len(nums) < 2:
                return False

            n = len(nums)
            for i in range(n):
                sum = 0
                for j in range(i, n):
                    sum += nums[j]
                    if j-i+1 >= 2 and sum % k == 0:
                        return True
            return False


# Optimal 
# Suppose at index i, the cumulative sum modulo k is mod. This means sum(nums[0:i+1]) % k = mod.
# Now, when we reach index j (where j > i), if the cumulative sum modulo k is also mod, it means sum(nums[0:j+1]) % k = mod.
# If sum(nums[0:i+1]) % k = sum(nums[0:j+1]) % k, then the difference between these two cumulative sums must be divisible by k. Therefore, sum(nums[i+1:j+1]) (the sum of elements from index i to index j) is divisible by k.

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
            if len(nums) < 2:
                return False

            n = len(nums)
            l, r = 0, 0
            sum = 0
            map = {0: -1}
            for i in range(n):
                sum += nums[i]
                mod = sum % k
                if mod in map:
                    if i - map[mod] >= 2:
                        return True
                else:
                    map[mod] = i
            return False 

            
