import typing
import pytest

from checkers.game import Game, Color, GameState
from checkers.board import Board, Cell


@pytest.fixture
def B_can_bet_5() -> Game:
    """This fixture determines board:

    |----------------|
    |__  __  __  __  |
    |  __w __w __w __|
    |__  __  __  __  |
    |  __w __w __w __|
    |__B __  __  __  |
    |  __  __  __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |----------------|

    Returns
    -------
    Game
    """
    size = 8
    board_table = [[Cell.EMPTY for i in range(size)] for j in range(size)]
    board = Board(8)
    board._board = board_table
    for row in range(1, 5, 2):
        for col in range(2, 8, 2):
            board.set_cell(row, col, Cell.WHITE)
    board.set_cell(4, 1, Cell.BLACK_QUEEN)
    game = Game(8)
    game.state = GameState.UNFINISHED
    game.board = board
    game.turn: Color = Color.BLACK
    game.black_count: int = 1
    game.white_count: int = 6

    return game


@pytest.fixture
def B_can_bet_5_expected() -> Game:
    """This fixture determines board:

    |----------------|
    |__  __  __  __  |
    |  __B __  __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |----------------|

    Returns
    -------
    Game
    """
    size = 8
    board_table = [[Cell.EMPTY for i in range(size)] for j in range(size)]
    board = Board(8)
    board._board = board_table
    board.set_cell(0, 1, Cell.BLACK_QUEEN)
    game = Game(8)
    game.state = GameState.BLACK_WON
    game.board = board
    game.turn: Color = Color.BLACK
    game.black_count: int = 1
    game.white_count: int = 0

    return game


def test_B_can_bet_5(
        B_can_bet_5: typing.Annotated[Game, pytest.fixture],
        B_can_bet_5_expected: typing.Annotated[Game, pytest.fixture]
) -> None:
    game = B_can_bet_5
    moves = game.get_all_moves()
    move = moves[1]
    game.make_move(move)
    game_expected = B_can_bet_5_expected

    assert game.state == game_expected.state
    assert game.black_count == game_expected.black_count
    assert game.white_count == game_expected.white_count
    assert game.tie_counter == game_expected.tie_counter

    for row in range(game.board.size):
        for col in range(game.board.size):
            game_cell = game.board.get_cell(row, col)
            game_expected_cell = game_expected.board.get_cell(row, col)
            assert game_cell == game_expected_cell


@pytest.fixture
def B_can_bet_4() -> Game:
    """This fixture determines board:

    |----------------|
    |__  __  __  __  |
    |  __  __w __  __|
    |__  __  __  __  |
    |  __w __w __  __|
    |__B __  __  __  |
    |  __w __w __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |----------------|

    Returns
    -------
    Game
    """
    size = 8
    board_table = [[Cell.EMPTY for i in range(size)] for j in range(size)]
    board = Board(8)
    board._board = board_table
    board.set_cell(1, 4, Cell.WHITE)
    board.set_cell(3, 2, Cell.WHITE)
    board.set_cell(3, 4, Cell.WHITE)
    board.set_cell(5, 2, Cell.WHITE)
    board.set_cell(5, 4, Cell.WHITE)
    board.set_cell(4, 1, Cell.BLACK_QUEEN)
    game = Game(8)
    game.state = GameState.UNFINISHED
    game.board = board
    game.turn: Color = Color.BLACK
    game.black_count: int = 1
    game.white_count: int = 5

    return game


@pytest.fixture
def B_can_bet_4_expected() -> Game:
    """This fixture determines board:

    |----------------|
    |__  __  __  __  |
    |  __  __w __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |__B __  __  __  |
    |  __  __  __  __|
    |__  __  __  __  |
    |  __  __  __  __|
    |----------------|

    Returns
    -------
    Game
    """
    size = 8
    board_table = [[Cell.EMPTY for i in range(size)] for j in range(size)]
    board = Board(8)
    board._board = board_table
    board.set_cell(1, 4, Cell.WHITE)
    board.set_cell(4, 1, Cell.BLACK_QUEEN)
    game = Game(8)
    game.state = GameState.UNFINISHED
    game.board = board
    game.turn: Color = Color.BLACK
    game.black_count: int = 1
    game.white_count: int = 1

    return game


def test_B_can_bet_4(
        B_can_bet_4: typing.Annotated[Game, pytest.fixture],
        B_can_bet_4_expected: typing.Annotated[Game, pytest.fixture]
) -> None:
    game = B_can_bet_4
    moves = game.get_all_moves()
    for move in moves:
        print(move)
    move = moves[1]
    print(game.board)
    game.make_move(move)
    game_expected = B_can_bet_4_expected
    print(game_expected.board)
    print(game.board)

    assert game.state == game_expected.state
    assert game.black_count == game_expected.black_count
    assert game.white_count == game_expected.white_count
    assert game.tie_counter == game_expected.tie_counter

    for row in range(game.board.size):
        for col in range(game.board.size):
            game_cell = game.board.get_cell(row, col)
            game_expected_cell = game_expected.board.get_cell(row, col)
            assert game_cell == game_expected_cell
