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

            
