from copy import deepcopy

from src.kata0003.fill_square import fill_square


class ConnectFourGame:
    def __init__(self):
        self.__cur_player = "x"

        # Fill a 7x7 square grid then drop the last row
        self.__board = fill_square([
            [None, None, None, None, None, None, None]
        ])
        self.__board.pop()


    def __find_four__(self, tiles):
        if len(tiles) > 1:
            direction = (
                tiles[-1][0] - tiles[-2][0],
                tiles[-1][1] - tiles[-2][1]
            )
            next_tile = (
                tiles[-1][0] + direction[0],
                tiles[-1][1] + direction[1]
            )
            
            # Check next tile is within bounds
            if (0 <= next_tile[0] < 7
                and 0 <= next_tile[1] < 6):
                pass



        ## RECURSIVE FUNCTION WITH PARAMETER `tiles` (list of coord tuples)
        ## check if `tiles` contains more than one item
        ## -- if so, subtract the last tile from the previous
        ##      to get direction of travel
        ##    add direction to last tile to get next tile
        ##    check it's within bounds
        ##    -- if so, check value at next tile matches last tile
        ##       -- if it matches, recurse with next tile appended to `tiles`
        ##          assign name `end_tile` to result and return
        ##       -- if no match, return tuple of last tile coords
        ## -- if `tiles` only conttains one item, then:
        ##    check if tile on top row
        ##    -- else, check if tile on bottom row
        ##    check if tile at far left
        ##    -- else, check if tile at far right
        ##    HORIZONTAL CHECK:
        ##      if not at far right,
        ##      -- add next tile to the right to `tiles` and recurse
        ##         assign name `end_right` to result
        ##      -- if not at far left,
        ##         add next tile to the left to `tiles` and recurse
        ##         assign name `end_left` to result
        ##      subtract `end_left` from `end_right`
        ##      if the difference is three,
        ##      -- add the next in-bounds tiles in either direction to the list
        ##           of possible winning moves for the current tile type, x or o
        ##    AND SO ON FOR VERTICAL CHECK
        ##    AND SO ON FOR FIRST DIAGONAL CHECK
        ##    AND SO ON FOR SECOND DIAGONAL CHECK

        # The above compiles a list of possible winning moves
        # but might be better with the final action being to check for a difference of four



    def get_board(self):
        return deepcopy(self.__board)


    def get_place_value(self, coords):
        return self.__board[coords[1]][coords[0]]


    def get_player(self):
        return self.__cur_player


    def play(self, column):
        counter_placed = False

        for row in range(6 - 1, -1, -1):
            if self.__board[row][column] is None:
                self.__board[row][column] = self.get_player()
                counter_placed = True
                break
        
        if not counter_placed:
            raise Exception("This column is full")

        self.__cur_player = "x" if self.get_player() == "o" else "o"


    def check_winner(self):
        return False