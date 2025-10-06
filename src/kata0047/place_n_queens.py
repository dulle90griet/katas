def place_n_queens(n: int) -> list[list[str]]:
    def backtrack(board: list[str], n: int, placed: int, ans: list[list[str]]) -> None:
        if placed == n:
            ans.append(board[:])
            return
        
        for col in range(n):
            row = placed
            collision = False
            for check_row in range(row-1, -1, -1):
                if board[check_row][col] == "Q":
                    collision = True
                dist = row - check_row
                if col >= dist and board[check_row][col-dist] == "Q":
                    collision = True
                if n - col - 1 >= dist and board[check_row][col+dist] == "Q":
                    collision = True
            if not collision:
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                backtrack(board, n, placed+1, ans)
                board[row] = board[row][:col] + "." + board[row][col+1:]
                
    board = ["." * n for _ in range(n)]
    ans = []
    backtrack(board, n, 0, ans)
    return ans