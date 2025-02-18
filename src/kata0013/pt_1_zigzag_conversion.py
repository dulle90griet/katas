""" A string is written in a zigzag with a number of rows, `r`, such that e.g. "bogdanovichstrolls" with `r = 4` will become:

    b     o     t
    o   n v   s r   s
    g a   i h   o l
    d     c     l

Read line by line, this becomes "botonvsrsgaiholdcl". Write code that will make this conversion. """

def zigzag_convert(s: str, r: int) -> str:
    if r < 2:
        return s
    
    zig_length = 2 * (r - 1)
    zig_width = r - 1
    
    rows = [""] * r
    for i in range(len(s)):
        cur_step = i % zig_length
        row = cur_step - max(0, 2 * (cur_step - zig_width))

        # If we wanted to calculate column, we could do so as follows for r > 2:
        #  cur_zig = idx // zig_length
        #  col = (cur_zig * zig_width) + cur_step - min(cur_step, zig_width)
        # But there is no need; row is sufficient.
        
        rows[row] += s[i]

    return "".join(rows)
