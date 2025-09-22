from collections import Counter

def group_anagrams(strs: list[str]) -> list[list[str]]:
    if not strs:
        return []
    groups = [[strs[0]]]
    counts = [Counter(strs[0])]

    for i, s in enumerate(strs[1:]):
        grouped = False
        for j, count in enumerate(counts):
            if count == Counter(s):
                groups[j].append(s)
                grouped = True
                break
        if not grouped:
            counts.append(Counter(s))
            groups.append([s])
    
    return groups
