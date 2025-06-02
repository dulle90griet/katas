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


# # alternative solution, counting up rather than down:
# 
# def generate_parentheses(n: int) -> list[str]:
#     bracket_stack, solutions = []
# 
#     def solve(n_opened: int, n_closed: int) -> None:
#         if n_opened == n_closed == n:
#             solutions.append("".join(bracket_stack))
#             return
# 
#         if n_opened < n:
#             bracket_stack.append("(")
#             solve(n_opened+1, n_closed)
#             bracket_stack.pop()
#
#         if n_closed < n_opened:
#             bracket_stack.append(")")
#             solve(n_opened, n_closed+1)
#             bracket_stack.pop()
#      
#     solve(0, 0)
#     return solutions
