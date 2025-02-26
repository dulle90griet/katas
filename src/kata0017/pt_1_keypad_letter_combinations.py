def letter_combinations(digits: str) -> list[str]:
    letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def unfurl_letters(start :int = 0):
        if start >= len(digits):
            return []
        if len(digits) - start == 1:
            return letters[digits[start]]
        
        unfurled = unfurl_letters(start+1)
        return [letter + sequence for sequence in unfurled
                for letter in letters[digits[start]]]

    return unfurl_letters()
