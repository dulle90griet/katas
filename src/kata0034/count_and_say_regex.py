import re

def count_and_say(n: int) -> str:
    s = "1"

    for _ in range(n - 1):
        # scan s with regex, constraining `*` with `\1` to track only repeats
        # group 0 is the full match; group 1 is the final character matched
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

    return s
