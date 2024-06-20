'''Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.'''



class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        count = [1]*n
        maxi = 1

        for i in range(n):
            for prev in range(i):
                if nums[i] > nums[prev]:
                    if dp[prev]+1 > dp[i]:
                        dp[i] = 1 + dp[prev]
                        count[i] = count[prev]
                    elif dp[prev]+1 == dp[i]:
                        count[i] = count[i] + count[prev]
                maxi = max(maxi, dp[i])

        count_of_lis = 0
        for i in range(n):
            if dp[i] == maxi:
                count_of_lis += count[i]
        return count_of_lis
        