class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp = [1] * N
        hash = [0] * N
        lastIndex = 0
        maxi = 0
        for i in range(N):
            hash[i] = i
            
            for prev in range(i):
                if arr[prev] < arr[i]:
                    if 1 + dp[prev] > dp[i]:
                        dp[i] = 1+dp[prev]
                        hash[i] = prev
                if dp[i] >maxi:
                    maxi = dp[i]
                    lastIndex = i
                    
        lis = []   
        while lastIndex != hash[lastIndex]:
            lis.append(arr[lastIndex])
            lastIndex = hash[lastIndex]
        lis.append(arr[lastIndex])
        return lis[::-1]
            