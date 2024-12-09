from src.kata0003.fill_square import fill_square

class ConnectFourGame:
    def __init__(self):
        self.__cur_player = "x"

        # Fill a 7x7 square grid then drop the last row
        self.__grid = fill_square([
            [None, None, None, None, None, None, None],
            [], [], [], [], []
        ])
        self.__grid.pop()


    def get_board(self):
        return self.__grid


    def get_player(self):
        pass


    def play(self):
        pass


    def check_winner(self):
        pass