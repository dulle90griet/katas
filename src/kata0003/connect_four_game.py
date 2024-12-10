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


    def __find_connected(self, places):
        if len(places) > 1:
            vector_of_travel = (
                places[-1][0] - places[-2][0],
                places[-1][1] - places[-2][1]
            )
            next_place = (
                places[-1][0] + vector_of_travel[0],
                places[-1][1] + vector_of_travel[1]
            )
            
            # Check current tile is within bounds
            if(0 <= places[-1][0] < 7
               and 0 <= places[-1][1] < 6):
                
                if(self.get_place_value(places[-1]) ==
                   self.get_place_value(places[-2])):
                    
                    return self.__find_connected(places + [next_place])
                
                elif self.get_place_value(places[-1]) == None:
                    return {
                        "places": places[:-1],
                        "next": places[-1]
                    }
            
            return {
                "places": places[:-1],
                "next": None
            }
        
        elif len(places) == 1:
            connections = []

            # Vertical check
            # Down
            next_place = (places[0][0], places[0][1] + 1)
            connection_down = self.__find_connected(places + [next_place])
            # Up
            next_place = (places[0][0], places[0][1] - 1)
            connection_up = self.__find_connected(places + [next_place])
            # Joined
            complete_vertical = {
                "places": (connection_down['places'][::-1][:-1]
                           + connection_up['places']),
                "next": [connection_down['next'],
                         connection_up['next']]
            }
            if len(complete_vertical['places']) > 2:
                connections.append(complete_vertical)

            # Horizontal check
            # Left
            next_place = (places[0][0] - 1, places[0][1])
            connection_left = self.__find_connected(places + [next_place])
            # Right
            next_place = (places[0][0] + 1, places[0][1])
            connection_right = self.__find_connected(places + [next_place])
            # Joined
            complete_horizontal = {
                "places": (connection_left['places'][::-1][:-1]
                            + connection_right['places']),
                "next": [connection_left['next'],
                         connection_right['next']]
            }
            if len(complete_horizontal['places']) > 2:
                connections.append(complete_horizontal)

            # Up-right diagonal check
            # Left + down
            next_place = (places[0][0] - 1, places[0][1] + 1)
            connection_left_down = self.__find_connected(places + [next_place])
            # Right + up
            next_place = (places[0][0] + 1, places[0][1] - 1)
            connection_right_up = self.__find_connected(places + [next_place])
            # Joined
            complete_up_right = {
                "places": (connection_left_down['places'][::-1][:-1]
                           + connection_right_up['places']),
                "next": [connection_left_down['next'],
                         connection_right_up['next']]
            }
            if len(complete_up_right['places']) > 2:
                connections.append(complete_up_right)

            # Down-right diagonal check
            # Left + up
            next_place = (places[0][0] - 1, places[0][1] - 1)
            connection_left_up = self.__find_connected(places + [next_place])
            # Right + down
            next_place = (places[0][0] + 1, places[0][1] + 1)
            connection_right_down = self.__find_connected(places + [next_place])
            # Joined
            complete_down_right = {
                "places": (connection_left_up['places'][::-1][:-1]
                           + connection_right_down['places']),
                "next": [connection_left_up['next'],
                         connection_right_down['next']]
            }
            if len(complete_down_right['places']) > 2:
                connections.append(complete_down_right)

            return connections


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
        ## -- if `tiles` only contains one item, then:
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
        # if places_to_check list is empty,
        # begin by selecting the topmost counter in each column
        # iterate over places_to_check
        # run find_connected(); if it returns None, remove the place from the list
        # if it returns a 3 and a next place,
        # remove the current place from the list and add that new one
        # if it returns a 4, return the winner

        return False