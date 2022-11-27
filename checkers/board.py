from enum import Enum


class Cell(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2
    BLACK_QUEEN = 3
    WHITE_QUEEN = 4


class Board:
    """
    A class to represent checkers board (SIZE)x(SIZE)

    ...

    Attributes
    ----------
    _board : list[list[type[Cell]]]
        board is a matrix of Cells
    board_state : type[BoardState]
        current state of the game

    Methods
    -------
    fill_initial():
        fill the _board by Cell.BLACK and Cell.WHITE.
    get_cell(row: int, col: int) -> Cell:
        Getter of cell with coords row and col.
    set_cell(row: int, col: int, cell: Cell) -> None:
        Set cell value with coords row and col.
    """

    SIZE = 8

    def __init__(self, size: int | None = None):
        """
        Set the board arrangenment in accordance with
        rules of English chekers.
        """
        self._board = [[Cell.EMPTY] * Board.SIZE for i in range(Board.SIZE)]
        self.fill_initial()
        if size is not None:
            Board.SIZE = size

    def fill_initial(self):
        """
        Fill the board by chekers:

        |----------------|
        |__b __b __b __b |
        |b __b __b __b __|
        |__b __b __b __b |
        |  __  __  __  __|
        |__  __  __  __  |
        |w __w __w __w __|
        |__w __w __w __w |
        |w __w __w __w __|
        |----------------|

        where ' ' is an empty black cell,
        '_' is an empty white cell,
        'b' is a black cell with the black cheker,
        'w' is a black cell with th white cheker.
        """
        for row in range(Board.SIZE // 2 - 1):
            for col in range(Board.SIZE):
                if row % 2 != col % 2:
                    self._board[row][col] = Cell.BLACK

        for row in range(Board.SIZE // 2 + 1, Board.SIZE):
            for col in range(Board.SIZE):
                if row % 2 != col % 2:
                    self._board[row][col] = Cell.WHITE

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Getter of cell with coords row and col.

        Parameters
        ----------
        row: int
            row index
        col: int
            column index

        Raises
        ------
        IndexError
            when row and col are not between 0 and Board.Size - 1

        Returns
        -------
        Cell
            cell type
        """
        if not 0 <= row < Board.SIZE or not 0 <= col < Board.SIZE:
            raise IndexError('row and col indices must be '
                             f'between 0 and {Board.SIZE - 1}.')

        return self._board[row][col]

    def set_cell(self, row: int, col: int, cell: Cell) -> None:
        """
        Set cell value with coords row and col.

        Parameters
        ----------
        cell: Cell
            type of cell is to set
        row: int
            row index
        col: int
            column index

        Raises
        ------
        IndexError
            when row and col are not between 0 and Board.Size - 1

        Returns
        -------
        None
        """
        if not 0 <= row < Board.SIZE or not 0 <= col < Board.SIZE:
            raise IndexError('row and col indices must be '
                             f'between 0 and {Board.SIZE - 1}.')

        self._board[row][col] = cell

    def __str__(self) -> str:
        cell_to_str = {
            Cell.EMPTY: ('__', '  '),
            Cell.BLACK: 'b ',
            Cell.WHITE: 'w ',
            Cell.BLACK_QUEEN: 'B ',
            Cell.WHITE_QUEEN: 'W ',
        }

        s = '|' + '--' * Board.SIZE + '|\n'
        for row in range(Board.SIZE):
            s += '|'
            for col in range(Board.SIZE):
                cell = self.get_cell(row, col)
                if cell == Cell.EMPTY:
                    s += cell_to_str[cell][(row + col) % 2]
                else:
                    s += cell_to_str[cell]
            s += '|\n'
        s += '|' + '--' * Board.SIZE + '|\n'

        return s


if __name__ == '__main__':
    board = Board()
    print(board)
