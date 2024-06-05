# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


import sys

class Solution:
    def commonChars(self, words):
        common = [sys.maxsize] * 26
        ans = []
        for word in words:
            temp = [0] * 26
            for j in word:
                temp[ord(j)-ord('a')] += 1
            for k in range(26):
                common[k] = min(common[k], temp[k])


        for i in range(26):
            while common[i] > 0:
                ans.append(chr(i + ord('a')))
                common[i] -= 1

        return ans

