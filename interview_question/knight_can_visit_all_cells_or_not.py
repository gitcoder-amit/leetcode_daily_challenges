
# Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must visit each square exactly once. Print the order of each cell in which they are visited.

# T --> O(8^(W*H))
# S --> O(W*H)
def is_safe(W, H, row, col, board):
    if row >= 0 and row <= H-1 and col >= 0 and col <= W-1 and board[row][col] == -1:
        return True
    return False

def solve(W, H, curx, cury, board, drow, dcol, step):
    if step == W*H:
        return True
    for i in range(8):
        newx = curx+drow[i]
        newc = cury+dcol[i]
        
        if is_safe(W, H, newx, newc, board):
            board[newx][newc] = 1
            if solve(W, H, newx, newc, board, drow, dcol, step+1):
                return True
            board[newx][newc] = -1
    return False



drow = [2, 1, -1, -2, -1, -2, 2, 1]
dcol = [1, 2, -2, -1, 2, 1, -1, -2]
step = 1
W = 5
H = 6
board = [[-1]*W for i in range(H)]
print(solve(W, H, 0, 0, board, drow, dcol, step))


