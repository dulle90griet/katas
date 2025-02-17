""" A string is written in a zigzag with a number of rows, `r`, such that e.g. "bogdanovichstrolls" with `r = 4` will become:

    b     o     t
    o   n v   s r   s
    g a   i h   o l
    d     c     l

Read line by line, this becomes "botonvsrsgaiholdcl". Write code that will make this conversion. """

def convert_index(idx: int, r: int) -> tuple[int]:
    zig_length = 2 * (r - 1)
    zig_width = r - 1
    cur_zig = idx // zig_length
    cur_step = idx % zig_length
    
    col = (cur_zig * zig_width) + cur_step - min(cur_step, zig_width)
    row = cur_step - max(0, 2 * (cur_step - zig_width))
    
    return row, col