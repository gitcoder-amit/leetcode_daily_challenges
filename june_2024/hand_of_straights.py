# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

 

# Constraints:

# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length
 

# Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/


# Brute force using map
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        m = {}
        for i in hand:
            m[i] = m.get(i, 0) + 1

        while m:
            first = min(m)
            for i in range(first, first+groupSize):
                if i not in m:
                    return False
                
                m[i] -= 1
                if m[i] == 0:
                    del m[i]
        return True

        

# Aproach 2 using MinHeap optimal
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        m = {}
        for i in hand:
            m[i] = m.get(i, 0) + 1

        minH = list(m.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i not in m:
                    return False
                
                m[i] -= 1
                if m[i] == 0:
                    # if i != minH[0]:  # optional
                    #     return False
                    heapq.heappop(minH)
        return True

        