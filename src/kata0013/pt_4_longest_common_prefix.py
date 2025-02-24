""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string. """

def longest_common_prefix(strs :list[str]) -> str:
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        for st in strs:
            if i == len(st) or st[i] != strs[0][i]:
                return st[:i]
    return strs[0]