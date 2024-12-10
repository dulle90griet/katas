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
            [None, None, None, None, None, None, None],
        ]

    def test_initialized_with_player_x(self):
        game = ConnectFourGame()
        assert game._ConnectFourGame__cur_player == "x"


class TestFindConnectedMethod:
    def test_find_connections_returns_empty_list_if_given_place_is_empty(self):
        game = ConnectFourGame()

        assert game._ConnectFourGame__find_connections([(3, 5)]) == []

    def test_find_connections_returns_empty_list_if_no_connections(self):
        game = ConnectFourGame()

        game._ConnectFourGame__board[5][3] = "x"

        assert game._ConnectFourGame__find_connections([(3, 5)]) == []

    def test_find_connections_finds_horizontal_connections(self):
        game = ConnectFourGame()
        expected = {
            "places": [(1, 5), (2, 5), (3, 5)],
            "next": [(0, 5), (4, 5)],
        }

        for col in range(1, 4):
            game._ConnectFourGame__board[5][col] = "o"

        assert expected in game._ConnectFourGame__find_connections([(3, 5)])

    def test_find_connections_finds_vertical_connections(self):
        game = ConnectFourGame()

        expected = {"places": [(3, 5), (3, 4), (3, 3)], "next": [None, (3, 2)]}
        for row in range(5, 2, -1):
            game._ConnectFourGame__board[row][3] = "x"
        assert expected in game._ConnectFourGame__find_connections([(3, 5)])

        expected = {
            "places": [(3, 5), (3, 4), (3, 3), (3, 2)],
            "next": [None, (3, 1)],
        }
        game._ConnectFourGame__board[2][3] = "x"
        assert expected in game._ConnectFourGame__find_connections([(3, 5)])

    def test_find_connections_finds_diagonal_connections(self):
        game = ConnectFourGame()
        game._ConnectFourGame__board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, "o"],
            [None, "o", None, None, None, "o", "x"],
            [None, "x", "o", None, "o", "o", "x"],
            [None, "o", "x", "o", "x", "o", "x"],
        ]

        expected_1 = {
            "places": [(1, 3), (2, 4), (3, 5)],
            "next": [(0, 2), None],
        }
        expected_2 = {
            "places": [(3, 5), (4, 4), (5, 3), (6, 2)],
            "next": [None, None],
        }
        result = game._ConnectFourGame__find_connections([(3, 5)])
        assert expected_1 in result
        assert expected_2 in result

        expected_3 = {"places": [(1, 4), (2, 5)], "next": [(0, 3), None]}
        result = game._ConnectFourGame__find_connections([(1, 4)])

    def test_find_connections_finds_mixed_connections(self):
        game = ConnectFourGame()
        game._ConnectFourGame__board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "x", "o", "x", None],
            [None, None, "x", "x", "x", "o", None],
            [None, None, "o", "x", "x", "x", "o"],
            ["o", None, "o", "o", "x", "o", "o"],
        ]

        expected_1 = {
            "places": [(2, 3), (3, 4), (4, 5)],
            "next": [(1, 2), None],
        }
        expected_2 = {
            "places": [(3, 4), (4, 3), (5, 2)],
            "next": [None, (6, 1)],
        }
        expected_3 = {"places": [(3, 4), (4, 4), (5, 4)], "next": [None, None]}
        expected_4 = {
            "places": [(3, 4), (3, 3), (3, 2)],
            "next": [None, (3, 1)],
        }
        result = game._ConnectFourGame__find_connections([(3, 4)])
        assert expected_1 in result
        assert expected_2 in result
        assert expected_3 in result
        assert expected_4 in result


class TestGetBoardMethod:
    def test_get_board_returns_current_board_state(self):
        game = ConnectFourGame()
        assert game.get_board() == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
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
            [None, None, "o", None, None, None, None],
        ]

    def test_get_board_returns_new_copy_of_board_state(self):
        game = ConnectFourGame()

        board = game.get_board()
        board[5][5] = "x"

        assert game._ConnectFourGame__board != board
        assert game._ConnectFourGame__board is not board


class TestGetPlaceValueMethod:
    def test_get_place_value_returns_None_if_place_empty(self):
        game = ConnectFourGame()

        assert game.get_place_value((0, 0)) is None
        assert game.get_place_value((3, 4)) is None
        assert game.get_place_value((6, 5)) is None

    def test_get_place_value_returns_counter_type_if_present(self):
        game = ConnectFourGame()

        game._ConnectFourGame__board[4][2] = "o"
        game._ConnectFourGame__board[5][5] = "x"

        assert game.get_place_value((2, 4)) is "o"
        assert game.get_place_value((5, 5)) is "x"


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
    def test_play_returns_nothing(self):
        game = ConnectFourGame()
        for i in range(7):
            assert game.play(i) is None

    def test_play_drops_counter_into_correct_column(self):
        game = ConnectFourGame()

        for col in range(len(game.get_board()[0])):
            game.play(col)
            cur_board = game.get_board()

            counter_found = False
            for row in range(len(cur_board)):
                if cur_board[row][col] is not None:
                    counter_found = True
                    break
            assert counter_found

    def test_dropped_counter_obeys_gravity(self):
        game = ConnectFourGame()

        game.play(0)
        cur_board = game.get_board()

        for row in range(len(cur_board) - 1):
            assert cur_board[row][0] is None
        assert cur_board[-1][0] is not None

        game.play(3)
        cur_board = game.get_board()

        for row in range(len(cur_board) - 1):
            assert cur_board[row][3] is None
        assert cur_board[-1][3] is not None

        game.play(0)
        cur_board = game.get_board()

        for row in range(len(cur_board) - 2):
            assert cur_board[row][0] is None
        assert cur_board[-2][0] is not None
        assert cur_board[-1][0] is not None

    def test_play_raises_exception_if_column_full(self):
        game = ConnectFourGame()

        for i in range(len(game.get_board())):
            game.play(5)
        with pytest.raises(Exception) as err:
            game.play(5)

        assert str(err.value) == "This column is full"

    def test_play_updates_player(self):
        game = ConnectFourGame()

        game.play(0)
        assert game.get_player() == "o"

        game.play(1)
        assert game.get_player() == "x"

        game.play(2)
        assert game.get_player() == "o"


class TestCheckWinner:
    def test_check_winner_returns_False_if_no_winner(self):
        game = ConnectFourGame()

        assert game.check_winner() is False

        game.play(2)  # x
        game.play(3)  # o
        game.play(4)  # x
        game.play(4)  # o
        game.play(2)  # x
        game.play(5)  # o
        game.play(2)  # x
        game.play(2)  # o
        game.play(5)  # x
        game.play(5)  # o

        assert game.check_winner() is False

    def test_check_winner_returns_winner_for_horizontal_4(self):
        game = ConnectFourGame()

        assert game.check_winner() is False

        game.play(1)  # x
        game.play(1)  # o
        game.play(2)  # x
        game.play(0)  # o
        game.play(3)  # x
        game.play(2)  # o
        game.play(4)  # x

        assert game.check_winner() == "x"

    def test_check_winner_returns_winner_for_vertical_4(self):
        game = ConnectFourGame()
        assert game.check_winner() is False
        game.play(6)  # x
        game.play(5)  # o
        game.play(6)  # x
        game.play(5)  # o
        game.play(6)  # x
        game.play(5)  # o
        game.play(4)  # x
        game.play(5)  # o
        assert game.check_winner() == "o"

        game = ConnectFourGame()
        assert game.check_winner() is False
        game.play(6)  # x
        game.play(5)  # o
        game.play(6)  # x
        game.play(5)  # o
        game.play(6)  # x
        game.play(5)  # o
        game.play(6)  # x
        assert game.check_winner() == "x"

    def test_check_winner_returns_winner_for_diagonal_4(self):
        game = ConnectFourGame()

        assert game.check_winner() is False

        game.play(2)  # x
        game.play(3)  # o
        game.play(4)  # x
        game.play(4)  # o
        game.play(2)  # x
        game.play(5)  # o
        game.play(2)  # x
        game.play(2)  # o
        game.play(5)  # x
        game.play(5)  # o
        game.play(6)  # x
        game.play(6)  # o
        game.play(6)  # x
        game.play(6)  # o

        assert game.check_winner() == "o"
