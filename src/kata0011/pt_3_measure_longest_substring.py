def longest_substring_len(self, s: str) -> int:
    maxlen = curlen = 1

    j = 0
    for i in range(1, len(s)):
        if s[i] in s[j:i]:
            j = i
            curlen = 1
            continue
        
        curlen += 1
        if curlen > maxlen:
            maxlen = curlen

    return maxlen