def longest_substring_len(self, s: str) -> int:
    if not s:
        return 0

    m = {s[0]: 0}
    maxlen = curlen = 1

    j = 0
    for i in range(1, len(s)):
        curchar = s[i]

        if curchar in s[j:i]:
            j = m[curchar] + 1
            m[curchar] = i
            curlen = i - j + 1
            continue
        
        m[curchar] = i
        curlen += 1

        if curlen > maxlen:
            maxlen = curlen

    return maxlen