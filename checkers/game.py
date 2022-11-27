from enum import Enum
from board import Board, Cell
from move import Move, WrongMoveError


class GameState(Enum):
    TIE = 0
    BLACK_WON = 1
    WHITE_WON = 2
    UNFINISHED = 3


class Color(Enum):
    BLACK = 1
    WHITE = 2


class Game:
    """
    A class to represent checkers board 8x8

    ...

    Attributes
    ----------
    board : Board
        board object
    game_state : type[GameState]
        current state of the game
    turn : Color
        Color of the chekers that have to go next

    Methods
    -------
    opponent() -> Color:
        Get the opponent of the current Color
    get_all_moves() -> list[Move]:
        Get the list off all possible moves for current turn
    get_moves(row: int, col: int) -> list[Move]:
        Find all moves for checker with coordinates row and col
    make_move(self, move: Move) -> None:
        Make a move and set board to the next turn
    """

    def __init__(self, size: int | None = None):
        """
        Creating a board. Black goes first.
        """
        self.board = Board(size)
        self.game_state = GameState.UNFINISHED
        self.turn = Color.BLACK

    def opponent(self) -> Color:
        """
        Get the opponent of the current Color

        Returns
        -------
        Color
        """
        if self.turn == Color.BLACK:
            return Color.WHITE
        return Color.BLACK

    def make_move(self, move: Move) -> None:
        """
        Make a move and set board to the next turn

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """
        if len(move.steps) == 1:
            first_step_len = abs(max(move.steps[0][0] - move.start[0],
                                     move.steps[0][1] - move.start[1]))

        if len(move.steps) == 1 and first_step_len == 1:
            self._make_one_step_move(move)
        else:
            self._make_beat_move(move)
        self._check_and_change_to_queen(move)

        self.turn = self.opponent()

    def _make_one_step_move(self, move: Move) -> None:
        """
        Make a one step move

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """
        row, col = move.steps[0]
        start_row, start_col = move.start
        cell = self.board.get_cell(start_row, start_col)
        self.board.set_cell(row, col, cell)
        self.board.set_cell(start_row, start_col, Cell.EMPTY)

    def _make_beat_move(self, move: Move) -> None:
        """
        Make a beating move

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """
        prev_row, prev_col = move.start
        prev_cell = self.board.get_cell(prev_row, prev_col)
        for step in move:
            row, col = step
            self.board.set_cell(
                    (prev_row + row) // 2,
                    (prev_col + col) // 2,
                    Cell.EMPTY)
            self.board.set_cell(prev_row, prev_col, Cell.EMPTY)
            self.board.set_cell(row, col, prev_cell)
            prev_row, prev_col = row, col

    def _check_and_change_to_queen(self, move: Move) -> None:
        """
        Change checker to queen if last step in the move
        is the first or the last row in the board

        Parameters
        ----------
        move : Move

        Returns
        -------
        None
        """
        last_row, last_col = move.steps[-1]
        if self.turn == Color.BLACK and last_row == self.board.SIZE - 1:
            self.board.set_cell(last_row, last_col, Cell.BLACK_QUEEN)
        elif self.turn == Color.WHITE and last_row == 0:
            self.board.set_cell(last_row, last_col, Cell.WHITE_QUEEN)

    def _is_turns_checker(self, cell: Cell) -> bool:
        """
        Check if the cell's checker belong to self.turn

        Returns
        -------
        bool
        """
        return (cell == Cell.BLACK or cell == Cell.BLACK_QUEEN) \
            and self.turn == Color.BLACK \
            or (cell == Cell.WHITE or cell == Cell.WHITE_QUEEN) \
            and self.turn == Color.WHITE

    def get_all_moves(self) -> list[Move]:
        """
        Get the list off all possible moves for current turn

        Returns
        -------
        list[Move]
            list consist of the all possible moves for current turn,
            [] if there are no moves
        """
        moves = []
        for row in range(self.board.SIZE):
            for col in range(self.board.SIZE):
                try:
                    moves += self.get_moves(row, col)
                except WrongMoveError:
                    continue

        return moves

    def get_moves(self, row: int, col: int) -> list[Move]:
        """
        Find all moves for checker with coordinates row and col.

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column number in the board

        Returns
        -------
        list[Move]
            list of possible moves for checker
            [] if there is no moves

        Raises
        ------
        WrongMoveError
            when cell type does not correspond to turn or
            row or col out of range(board.SIZE)
        """
        if not 0 <= row < self.board.SIZE \
                or not 0 <= col < self.board.SIZE:
            raise WrongMoveError('row and col must be in the' +
                                 'range(self.board.SIZE)')

        cell = self.board.get_cell(row, col)
        if not self._is_turns_checker(cell):
            raise WrongMoveError('cell type does not correspond turn\'s color')

        moves = []
        for step_sequence in self._get_steps(row, col):
            moves.append(Move((row, col), step_sequence))

        return moves

    def _cell_with_opponent(self, cell: Cell) -> bool:
        """
        Check if the cell with opponent checker.

        Returns
        -------
        bool
        """
        if self.turn == Color.BLACK \
                and cell in (Cell.WHITE, Cell.WHITE_QUEEN):
            return True
        if self.turn == Color.WHITE \
                and cell in (Cell.BLACK, Cell.BLACK_QUEEN):
            return True
        return False

    def _dfs_find_beat_steps(
                self,
                row: int,
                col: int,
                dirs: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
        """
        Find all steps that beat opponent's checkers

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board
        dirs : list[tuple[int, int]]
            list of possible directions to a move

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """
        res = []
        for dir in dirs:
            tmp = []
            r1, c1 = row + dir[0], col + dir[1]
            try:
                cell = self.board.get_cell(r1, c1)
            except IndexError:
                continue
            if self._cell_with_opponent(cell):
                r2, c2 = r1 + dir[0], c1 + dir[1]
                try:
                    next_cell = self.board.get_cell(r2, c2)
                except IndexError:
                    continue
                if next_cell == Cell.EMPTY:
                    new_dirs = []
                    for d in dirs:
                        if not (d[0] == -dir[0] and d[1] == -dir[1]):
                            new_dirs.append(d)
                    res1 = self._dfs_find_beat_steps(r2, c2, new_dirs)
                    tmp1 = [(r2, c2)]
                    if not res1:
                        tmp += [tmp1]
                    for e in res1:
                        tmp.append(tmp1 + e)
                    res += tmp
        return res

    def _find_not_beat_steps(
                self,
                row: int,
                col: int,
                dirs: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
        """
        Find all one step and not beating steps

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board
        dirs : list[tuple[int, int]]
            list of possible directions to a move

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """
        res = []
        for dir in dirs:
            r1, c1 = row + dir[0], col + dir[1]
            try:
                cell = self.board.get_cell(r1, c1)
            except IndexError:
                continue
            if cell == Cell.EMPTY:
                res.append([(r1, c1)])

        return res

    def _get_steps(self, row: int, col: int) -> list[Move]:
        """
        Find all possible steps for checker.
        It is consider that there is a checker in the cell!

        Parameters
        ----------
        row : int
            0-indexed row number in the board
        col : int
            0-indexed column numer in the board

        Returns
        -------
        list[list[tuple[int, int]]]
            list of lists of steps for each possible move
        """
        dirs = []
        cell = self.board.get_cell(row, col)
        if cell == Cell.BLACK:
            dirs = [
                (1, -1),
                (1, 1),
            ]
        elif cell == Cell.WHITE:
            dirs = [
                (-1, -1),
                (-1, 1),
            ]
        elif cell in (Cell.BLACK_QUEEN, Cell.WHITE_QUEEN):
            dirs = [
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
            ]
        steps = self._find_not_beat_steps(row, col, dirs)
        steps += self._dfs_find_beat_steps(row, col, dirs)

        return steps


if __name__ == '__main__':
    game = Game()
    moves = game.get_all_moves()
    while moves:
        print(game.board)
        print(game.turn)
        for move in moves:
            print(move)
        print('Input start_row and start_col for move:')
        start_row, start_col = tuple(map(int, input().strip().split()))
        print('Input row and col for the first step of the move:')
        row, col = tuple(map(int, input().strip().split()))
        for move in moves:
            if move.start == (start_row, start_col):
                if move.steps[0] == (row, col):
                    game.make_move(move)
                    moves = game.get_all_moves()
                    break
