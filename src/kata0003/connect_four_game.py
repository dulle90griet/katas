from copy import deepcopy

from src.kata0003.fill_square import fill_square


class ConnectFourGame:
    def __init__(self):
        self.__cur_player = "x"
        self.__places_to_check = []

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

            if self.get_place_value(places[0]) is None:
                return connections

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
        print(f"==>> self.__places_to_check: {self.__places_to_check}")
        if not self.__places_to_check:
            for column in range(7):
                if self.get_place_value((column, 6 - 1)):
                    for row in range(6 - 2, -1, -1):
                        if self.get_place_value((column, row)) is None:
                            self.__places_to_check.append((column, row + 1))
                            break
        print(f"==>> self.__places_to_check: {self.__places_to_check}")

        next_to_check = []
        
        for place in self.__places_to_check:
            connections = self.__find_connected([place])
            
            for connection in connections:
                print(f"==>> connection: {connection}")
                if len(connection['places']) == 3:
                    next_to_check += [next for next in connection['next']
                                      if next is not None]
                elif len(connection['places']) >= 4:
                    print(f"==>> self.get_place_value(connection['places'][0]): {self.get_place_value(connection['places'][0])}")
                    return self.get_place_value(connection['places'][0])
            
            self.__places_to_check.remove(place)
            self.__places_to_check += next_to_check
        print(f"==>> self.__places_to_check: {self.__places_to_check}")

        return False