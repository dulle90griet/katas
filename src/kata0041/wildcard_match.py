def wildcard_match(s: str, p: str) -> bool:
    matches = []

    def dfs(s_idx, p_idx):
        if bool(matches):
            return

        if p_idx >= len(p) and s_idx >= len(s):
            matches.append(1)
            return
        if s_idx >= len(s):
            if all([c == "*" for c in p[p_idx:]]):
                matches.append(1)
            return
        if p_idx >= len(p):
            return

        match p[p_idx]:
            case "*":
                dfs(s_idx+1, p_idx+1) # Wildcard matched single char; continue to next string and pattern chars
                dfs(s_idx+1, p_idx) # Wildcard match group continues to next string char
                if p_idx < len(p) - 1:
                    dfs(s_idx, p_idx+1) # Wildcard matched empty sequence; continue to next pattern char
            case "?":
                dfs(s_idx+1, p_idx+1)
            case _:
                if s[s_idx] == p[p_idx]:
                    dfs(s_idx+1, p_idx+1)
                else:
                    return
    
    dfs(0, 0)

    return bool(matches)