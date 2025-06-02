def solve(opening: int, closing: int, solutions: list[str], cur_solution: str=""):
    if opening == 0 and closing == 0:
        solutions.append(cur_solution)
        return

    if opening:
        solve(opening-1, closing, solutions, cur_solution+"(")

        if opening == closing:
            return
    
    if closing:
        solve(opening, closing-1, solutions, cur_solution+")")


def generate_parentheses(n: int) -> list[str]:
    solutions = []
    solve(n, n, solutions)
    return solutions
