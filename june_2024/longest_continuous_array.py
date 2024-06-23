'''
    1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

    Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

'''


# T --> O(n*n)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        maxlen = 0
        min_diff = 100000000000
        for i in range(n):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i, n):
                maxi = max(maxi, nums[j])
                mini = min(mini, nums[j])
                diff = abs(maxi-mini)
                if diff <= limit:
                    maxlen = max(maxlen, j-i+1)
        return maxlen

        l = 0
        r = 0
        n = len(nums)
        mx = 0
        mn = 100000000
        m = {}
        maxlen = 0
        while r < n:
            m[nums[r]] = m.get(nums[r], 0) + 1
            mx = max(mx, nums[r])
            mn = min(mn, nums[r])
            diff = abs(mx-mn)
            while diff > limit:
                m[nums[l]] -= 1
                if m[nums[l]] == 0:
                    del m[nums[l]]

                mx = max(m)
                mn = min(m)
                diff = abs(mx-mn)
                l += 1
            
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen



# T -> O(2N)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        mx = 0
        mn = 100000000
        m = {}
        maxlen = 0
        while r < n:
            m[nums[r]] = m.get(nums[r], 0) + 1
            mx = max(mx, nums[r])
            mn = min(mn, nums[r])
            diff = abs(mx-mn)
            while diff > limit:
                m[nums[l]] -= 1
                if m[nums[l]] == 0:
                    del m[nums[l]]

                mx = max(m)
                mn = min(m)
                diff = abs(mx-mn)
                l += 1
            
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
        