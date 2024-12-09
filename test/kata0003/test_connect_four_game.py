import pytest

from src.kata0003.connect_four_game import ConnectFourGame


class TestInitialization:
    def test_initialized_with_7_by_6_matrix(self):
        game = ConnectFourGame()
        assert game._ConnectFourGame__grid == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ]

    
    def test_initialized_with_player_x(self):
        game = ConnectFourGame()
        assert game._ConnectFourGame__cur_player == "x"


class TestGetBoardMethod:
    def test_get_board_returns_current_board_state(self):
        game = ConnectFourGame()
        assert game.get_board() == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ]

        for row in range(len(game.__ConnectFourGame__board)):
            for col in range(len(row)):
                if col == 2 and row >= 2:
                    game.__ConnectFourGame__board[row][col] = "o"
        assert game.get_board() == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, "o", None, None, None, None],
            [None, None, "o", None, None, None, None],
            [None, None, "o", None, None, None, None],
            [None, None, "o", None, None, None, None]
        ]



class TestGetPlayerMethod:
    @pytest.mark.skip
    def test_get_player_returns_current_player(self):
        pass


class TestPlayMethod:
    @pytest.mark.skip
    def test_play_drops_counter_into_correct_column(self):
        pass


    @pytest.mark.skip
    def test_dropped_counter_obeys_gravity(self):
        pass


    @pytest.mark.skip
    def test_play_raises_exception_if_column_full(self):
        pass


    @pytest.mark.skip
    def test_play_returns_nothing(self):
        pass


class TestCheckWinner:
    @pytest.mark.skip
    def test_check_winner_returns_False_if_no_winner(self):
        pass

    
    @pytest.mark.skip
    def test_check_winner_returns_winner_for_horizontal_4(self):
        pass


    @pytest.mark.skip
    def test_check_winner_returns_winner_for_vertical_4(self):
        pass


    @pytest.mark.skip
    def test_check_winner_returns_winner_for_diagonal_4(self):
        pass

