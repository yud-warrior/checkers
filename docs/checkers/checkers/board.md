Module checkers.board
=====================
This module is for representing checkers board.

Class Cell(Enum) describes all possible conditions of the board's cell.

Class Board is to represent and initially fill the board and allow to
read and set cell values.

This file can also be imported as module and contains the following
classes:

    * Cell - Enum that represents cell values
    * Board - represent checkers board

Classes
-------

`Board(size: int = 0)`
:   A class to represent checkers board (SIZE)x(SIZE)
    
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
    
    Set the board arrangenment in accordance with
    rules of English chekers.

    ### Class variables

    `SIZE`
    :

    ### Methods

    `fill_initial(self)`
    :   Fill the board 8x8 (example) by chekers:
        
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

    `get_cell(self, row: int, col: int) ‑> checkers.board.Cell`
    :   Getter of cell with coords row and col.
        
        Parameters
        ----------
        row: int
            row index
        col: int
            column index
        
        Raises
        ------
        IndexError
            when row and col are not between 0 and size - 1
        
        Returns
        -------
        Cell
            cell type

    `set_cell(self, row: int, col: int, cell: checkers.board.Cell) ‑> None`
    :   Set cell value with coords row and col.
        
        Parameters
        ----------
        row: int
            row index
        col: int
            column index
        cell: Cell
            type of cell is to set
        
        Raises
        ------
        IndexError
            when row and col are not between 0 and Board.Size - 1
        
        Returns
        -------
        None

`Cell(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `BLACK`
    :

    `BLACK_QUEEN`
    :

    `EMPTY`
    :

    `WHITE`
    :

    `WHITE_QUEEN`
    :