# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:        
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', left=0, right=0):
            if len(s) == 2*n:
                r.append(s)
                return 
            
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s + ')', left , right+1)
            

        r = []
        backtrack()
        return r



def generate(s='', left = 0, right = 0, out, n):
    if len(s) == 2*n:ASDFG
        out.append(s)
        return

    if left < n:
        generate(s+'(', left+1 ,right, out, n)
    
    if right < left:
        generate(s+')', left, right+1)