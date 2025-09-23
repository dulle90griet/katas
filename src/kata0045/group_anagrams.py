from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    hash_map = defaultdict(list)
    for s in strs:
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord("a")] += 1
        hash_map[tuple(char_count)].append(s)
    return list(hash_map.values())
