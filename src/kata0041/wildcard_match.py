def wildcard_match(s: str, p: str) -> bool:
    if len(s) == 0:
        return all([c == "*" for c in p])

    s_traversed, p_traversed = [-1], [-1]


    def dfs(s_idx, p_idx):
        if p_traversed[-1] < len(p) - 1 and s_idx - 1 >= s_traversed[-1]:
            s_traversed[-1] = s_idx - 1
            p_traversed[-1] = p_idx - 1
        if s_idx == len(s) or p_idx == len(p):
            return

        match p[p_idx]:
            case "*":
                dfs(s_idx+1, p_idx)
                dfs(s_idx+1, p_idx+1)
                dfs(s_idx, p_idx+1)
            case "?":
                dfs(s_idx+1, p_idx+1)
            case _:
                if s[s_idx] == p[p_idx]:
                    dfs(s_idx+1, p_idx+1)
                else:
                    return
    

    dfs(0, 0)

    return s_traversed[-1] == len(s) - 1 and (p_traversed[-1] == len(p) -1 or p_traversed[-1] == len(p) - 2 and p[-1] == "*")