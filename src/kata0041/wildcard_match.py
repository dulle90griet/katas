def wildcard_match(s: str, p: str) -> bool:
    s_idx = p_idx = 0
    last_match = star_p = -1

    while s_idx < len(s):
        if p_idx < len(p) and (s[s_idx] == p[p_idx] or p[p_idx] == "?"):
            s_idx += 1
            p_idx += 1
        elif p_idx < len(p) and p[p_idx] == "*":
            star_p = p_idx
            p_idx += 1
            last_match = s_idx
        elif star_p != -1:
            p_idx = star_p + 1
            last_match += 1
            s_idx = last_match
        else:
            return False

    while p_idx < len(p) and p[p_idx] == "*":
        p_idx += 1
    
    return p_idx == len(p)
