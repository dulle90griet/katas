def count_and_say(n: int) -> str:
        s = "1"

        while n > 1:
            encoded = []
            count = 0
            for i in range(len(s)):
                count += 1
                if i == len(s) - 1 or s[i+1] != s[i]:
                    encoded.append(f"{count}{s[i]}")
                    count = 0
            
            s = "".join(encoded)
            n -= 1

        return s
