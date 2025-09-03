def wildcard_match(s: str, p: str) -> bool:
    s_idx = p_idx = 0
    last_star_match = star_p_idx = -1

    while s_idx < len(s):
        if p_idx < len(p) and (s[s_idx] == p[p_idx] or p[p_idx] == "?"):
            s_idx += 1
            p_idx += 1
        elif p_idx < len(p) and p[p_idx] == "*":
            last_star_match = s_idx
            star_p_idx = p_idx
            p_idx += 1
        elif star_p_idx == -1:
            last_star_match += 1
            s_idx = last_star_match
            p_idx = star_p_idx = 1
        else:
            return False

    while p_idx < len(p) and p[p_idx] == "*":
        p_idx += 1
    
    return p_idx == len(p)
