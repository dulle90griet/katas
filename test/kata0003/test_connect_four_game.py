import pytest

from src.kata0003.connect_four_game import ConnectFourGame


class TestInitialization:
    def test_initialized_with_7_by_6_matrix(self):
        pass


class TestGetBoardMethod:
    def test_get_board_returns_current_board_state(self):
        pass


class TestGetPlayerMethod:
    def test_get_player_returns_current_player(self):
        pass


class TestPlayMethod:
    def test_play_drops_counter_into_correct_column(self):
        pass


    def test_dropped_counter_obeys_gravity(self):
        pass


    def test_play_raises_exception_if_column_full(self):
        pass


    def test_play_returns_nothing(self):
        pass


class TestCheckWinner:
    def test_check_winner_returns_False_if_no_winner(self):
        pass

    
    def test_check_winner_returns_winner_for_horizontal_4(self):
        pass


    def test_check_winner_returns_winner_for_vertical_4(self):
        pass


    def test_check_winner_returns_winner_for_diagonal_4(self):
        pass

