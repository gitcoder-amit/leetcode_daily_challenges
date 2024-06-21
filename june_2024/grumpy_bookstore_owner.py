'''There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
'''


# Brute Force

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxi = 0
        l = 0
        r = minutes-1
        for i in range(len(customers)):
            sum = 0
            for j in range(len(customers)):
                if j >= l and j <= r:
                    sum += customers[j]
                
                elif grumpy[j] == 1:
                    sum += 0
                else:
                    sum += customers[j]
            l += 1
            r += 1
            maxi = max(maxi, sum)
        return maxi


# Optimal

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxi = 0
        l = 0
        r = minutes-1
        sum = 0

        for i in range(len(customers)):
            if i >= l and i <= r:
                    sum += customers[i]
                
            elif grumpy[i] == 1:
                sum += 0
            else:
                sum += customers[i]
        
        maxi = sum
        n = len(customers)
        while r < n:
            l += 1 
            r += 1

            if l-1 < n and grumpy[l-1] == 1:
                sum -= customers[l-1]
    
            if r < n and grumpy[r] == 1:
                sum += customers[r]
            maxi = max(sum, maxi)

        return maxi