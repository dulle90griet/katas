import pytest

from src.kata0003.connect_four_game import ConnectFourGame


class TestInitialization:
    def test_initialized_with_7_by_6_matrix(self):
        game = ConnectFourGame()
        assert game._ConnectFourGame__board == [
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

        game = ConnectFourGame()
        for row in range(2, len(game._ConnectFourGame__board)):
            game._ConnectFourGame__board[row][2] = "o"
        assert game.get_board() == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, "o", None, None, None, None],
            [None, None, "o", None, None, None, None],
            [None, None, "o", None, None, None, None],
            [None, None, "o", None, None, None, None]
        ]

    
    def test_get_board_returns_new_copy_of_board_state(self):
        game = ConnectFourGame()

        board = game.get_board()
        board[5][5] = "x"

        assert game._ConnectFourGame__board != board
        assert game._ConnectFourGame__board is not board


class TestGetPlayerMethod:
    def test_get_player_returns_current_player(self):
        game = ConnectFourGame()
        assert game.get_player() == "x"

        game._ConnectFourGame__cur_player = "o"
        assert game.get_player() == "o"


    def test_get_player_returns_new_copy_of_cur_player(self):
        game = ConnectFourGame()

        player = game.get_player()
        player = "test"

        assert game._ConnectFourGame__cur_player != player
        assert game._ConnectFourGame__cur_player is not player


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

