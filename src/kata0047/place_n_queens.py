def place_n_queens(n: int) -> list[list[str]]:
    def backtrack(queens, xy_sum, xy_diff) -> None:
        row = len(queens)

        if row == n:
            ans.append(queens[:])

        for col in range(n):
            if col not in queens and col+row not in xy_sum and col-row not in xy_diff:
                backtrack(queens+[col], xy_sum+[col+row], xy_diff+[col-row])

    ans = []
    backtrack([], [], [])

    return [["."*col + "Q" + "."*(n-col-1) for col in sol] for sol in ans]
