# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# Approach 1 T--> O(n*n) S-> O(n)
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    maxi =1
    dp = [1] * n
    for i in range(n):
        for prev in range(i):
            if nums[prev] < nums[i]:
                dp[i] = max(dp[i], 1+dp[prev])
            maxi = max(maxi, dp[i])
    # n = len(nums)
    # return self.helper1(nums, n)
    return maxi



# Approach 2
# recusion  T--> O(2**n) S--> O(N) for recurive stack
def helper(self, i, nums, n, prev):
        if i == n:
            return 0
        take = -sys.maxsize.
        not_take = self.helper(i+1, nums, n, prev)
        if prev == -1 or nums[i] > nums[prev]:
            take = self.helper(i+1, nums, n, i) + 1

        return max(take, not_take)
        


def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    return self.helper(0, nums, len(nums) , -1)



# Memoization

 def helper(self, i, nums, n, prev, dp):
        if i == n:
            return 0
        if dp[i][prev+1] != -1:
            return dp[i][prev+1]
        take = -sys.maxsize
        not_take = self.helper(i+1, nums, n, prev, dp)
        if prev == -1 or nums[i] > nums[prev]:
            take = self.helper(i+1, nums, n, i, dp) + 1

        dp[i][prev+1] = max(take, not_take)
        return dp[i][prev+1]


def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp  = [[-1 for j in range(n+1)] for i in range(n)]
    return self.helper(0, nums, len(nums) , -1, dp)
    # return self.helper1(nums, n)


# Tabulation

def helper1(self, nums, n):
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(n-1, -1, -1):
        for prev in range(i-1, -2, -1):
            not_take = dp[i+1][prev+1]
            take = -sys.maxsize
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dp[i+1][i+1]
            dp[i][prev+1] = max(take, not_take)
    return dp[0][0]

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    return self.helper1(nums, n)
