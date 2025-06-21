# Minimum Deletions to Make String K-Special


'''3085. Minimum Deletions to Make String K-Special
Medium
You are given a string s and an integer k. A string is called k-special if it contains at most k distinct characters.
Return the minimum number of characters you need to delete from s to make it k-special. If s is already k-special, return 0.
Example 1:
Input: s = "abcabc", k = 2
Output: 4
Explanation: We can delete 4 characters to make the string "abab" which is 2-special.
Example 2:
Input: s = "aabbcc", k = 1
Output: 4
Explanation: We can delete 4 characters to make the string "aa" which is 1-special.
Example 3:
Input: s = "aabbcc", k = 3
Output: 0

Constraints:
1 <= s.length <= 105
1 <= k <= 26 '''


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = {}
        for i in word:
            freq[i] = freq.get(i, 0) + 1

        res = 1000000
        for i in freq:  # consider every i as minimum freq element
            deletion = 0
            for j in freq:
                if freq[j] < freq[i]:
                    deletion += freq[j]
                elif freq[j]-freq[i] > k:
                    deletion += (freq[j]-(freq[i]+k))
            res = min(res, deletion)
        return res



'''Let n be the length of the string word, and let C be the size of the character set, which is 26 in this case.

Time complexity: O(n+C 
2
 ).

We enumerate each character and calculate the number of deleted characters.

Space complexity: O(C).

The space complexity when using a hash table is O(C).'''

        