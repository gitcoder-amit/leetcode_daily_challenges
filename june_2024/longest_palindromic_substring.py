# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"


def longestPalindromeSubstring(s: str) -> str:
        n = len(s)
        r = ''
        for i in range(n):
            s1 = ''
            for j in range(i, n):
                s1 += s[j]
                if s1 == s1[::-1] and len(s1)>len(r):
                    r = s1
                    print(r)
        return r

        