def find_first_str_in_str(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        for k in range(len(needle)+1):
            if k == len(needle):
                return i
            if i + k == len(haystack) or haystack[i+k] != needle[k]:
                break
    return -1