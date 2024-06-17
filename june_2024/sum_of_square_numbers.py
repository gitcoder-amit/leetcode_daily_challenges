'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
'''
def judgeSquareSum(self, c: int) -> bool:
        m = {}
        m[0] = 1
        if c == 0:
            return True
        for i in range(1, floor(math.sqrt(c))+1):
            m[i*i] = 1

        for i in range(1,floor(math.sqrt(c))+1):
            a = i*i
            if (c - a) in m:
                return True
        
        return False


class Solution:
    def binary_search(self,b):
        start = 0
        end = b
        while start <= end:
            mid = (start+end)//2
            if mid * mid == b:
                return True
            elif mid*mid < b:
                start = mid+1
            else:
                end = mid-1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, floor(math.sqrt(c))+1):
            a = i * i
            rem = c - a
            if self.binary_search(rem) == True:
                return True
        return False


        