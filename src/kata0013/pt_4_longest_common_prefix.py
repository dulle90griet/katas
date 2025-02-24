""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string. """

def longest_common_prefix(strs :list[str]) -> str:
    if not strs:
        return ""
    
    i = 0
    while i < len(strs[0]):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j-1][i] != strs[j][i]:
                return strs[0][:i]  
        i += 1
    return strs[0][:i]