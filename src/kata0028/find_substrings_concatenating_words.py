def find_substrings_concatenating_all_words(
    self,
    s: str,
    words: list[str]
) -> list[int]:
    word_len = len(words[0])
    substr_len = word_len * len(words)
    indexes = []

    def get_frequencies(word_list: list[str]) -> dict:
        frequencies = {}
        for word in word_list:
            frequencies[word] = frequencies.get(word, 0) + 1
        return frequencies

    frequencies = get_frequencies(words)

    for i in range(len(s) - substr_len + 1):
        parts = [s[start:start+word_len] for start in range(i, i + substr_len, word_len)]
        if get_frequencies(parts) == frequencies:
            indexes.append(i)

    return indexes
