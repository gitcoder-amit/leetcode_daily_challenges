# 51. N-Queens

'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 '''

class Solution:
    def is_safe(self, row, col, board, n):
        def upper_diagonal_check(row, col):
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            return True
        
        def lower_diagonal_check(row, col):
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            return True
        
        def left_column_check(row, col):
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
            return True
        
        return upper_diagonal_check(row, col) and lower_diagonal_check(row, col) and left_column_check(row, col)

    def helper(self,n, col, board, ans):
        if col == n:
            ans.append([''.join(row) for row in board])
            return
        for row in range(n):
            if self.is_safe(row, col, board, n):
                board[row][col] = 'Q'
                self.helper(n, col+1, board, ans)
                board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        ans = []
        self.helper(n,0, board, ans)    
        return ans
    
        