def count_and_say(n: int) -> str:
    def r_l_encode(n: int, s: str="1") -> str:
        if n == 1:
            return s

        result = ""
        count = 0
        for i in range(len(s)):
            count += 1
            if i == len(s) - 1 or s[i + 1] != s[i]:
                result += f"{count}{s[i]}"
                count = 0
        
        return r_l_encode(n-1, result)
    
    return r_l_encode(n)
