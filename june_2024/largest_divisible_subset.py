# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1]*n
        hash = [0]*n
        lastIndex = 0
        nums.sort()
        maxi =0 
        for i in range(n):
            hash[i] = i

            for prev in range(i):
                if nums[i]%nums[prev] == 0:
                    if 1+dp[prev] > dp[i]:
                        dp[i] = 1 + dp[prev]
                        hash[i] = prev
                if dp[i] > maxi:
                    maxi = dp[i]
                    lastIndex = i
        
        ans = []
        while lastIndex != hash[lastIndex]:
            ans.append(nums[lastIndex])
            lastIndex = hash[lastIndex]
        ans.append(nums[lastIndex])
        return ans