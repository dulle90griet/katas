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


    def get_board(self):
        return deepcopy(self.__board)


    def get_player(self):
        return self.__cur_player


    def play(self, column):
        for row in range(len(self.__board) - 1, -1, -1):
            if self.__board[row][column] is None:
                self.__board[row][column] = self.get_player()
                break


    def check_winner(self):
        pass