def count_and_say(n: int) -> str:
    def r_l_encode(n: int, val: str="1") -> str:
        if n == 1:
            return val

        result = ""
        count = 0
        for i in range(len(val)):
            count += 1
            if i == len(val) - 1 or val[i + 1] != val[i]:
                result += f"{count}{val[i]}"
                count = 0
        
        return r_l_encode(n-1, result)
    
    return r_l_encode(n)
