# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105


class Solution:
    def reverse(self, arr):
        n = len(arr)
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    def reverseString(self, s) -> None:
        self.reverse(s)