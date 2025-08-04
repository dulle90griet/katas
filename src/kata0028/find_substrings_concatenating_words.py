def find_substrings_concatenating_all_words(
    self,
    s: str,
    words: list[str]
) -> list[int]:
    word_len = len(words[s])
    substr_len = word_len * len(words)
    indexes = []

    for i in range(len(s) - substr_len + 1):
        found = set()

        for j in range(len(words)):
            start = i + word_len * j
            end = start + word_len

            word = s[start:end]

            if word not in words:
                break
            if word in found:
                break

            found.add(word)

        if len(found) == len(words):
            indexes.append(i)
    
    return indexes