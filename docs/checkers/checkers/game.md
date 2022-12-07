Module checkers.game
====================
This module is for simulating the English checkers game.

Class Game represents a simulation of the checkers game and allows
get all possible moves for the current side (current turn), make
and cancel moves (with previous game state recovery).

This file can also be imported as module and contains the following
classes:

    * GameState - (Enum) describes all possible states of the game
    * Color - represents player's color ( side in the game).
    * Game - represent a simulation of the game.

Classes
-------

`Color(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `BLACK`
    :

    `WHITE`
    :

`Game(size: int = 0)`
:   A class to represent checkers board 8x8
    
    ...
    
    Attributes
    ----------
    board : Board
        board object
    state : type[GameState]
        current state of the game
    turn : Color
        Color of the chekers that have to go next
    last_changes : list[list[tuple[int, int, Cell]]]
        Last item is a tuple of row, column and initial value of the cell
        that was changed last. Previous item - last before last and so on.
    black_count : int
        Number of black checkers on the board
    white_count : int
        Number of white checkers on the board
    tie_counter : int
        Number of last serial moves when
        black_count and white_count were not changed
    tie_max : int
        Maximum value of the tie_counter
        If tie_counter == tie_max then game finishes with the tie
    
    Methods
    -------
    opponent() -> Color:
        Get the opponent of the current Color
    get_all_moves() -> list[Move]:
        Get the list off all possible moves for current turn
    make_move(self, move: Move) -> None:
        Make a move and set board to the next turn
    undo() -> None:
        Cancels last move and recover previous state and board
    
    Creating a board. Black goes first.

    ### Methods

    `get_all_moves(self) ‑> list[checkers.move.Move]`
    :   Get the list off all possible moves for current turn
        
        Returns
        -------
        list[Move]
            list consist of the all possible moves for current turn,
            [] if there are no moves

    `make_move(self, move: checkers.move.Move) ‑> None`
    :   Make a move and set board to the next turn
        
        Parameters
        ----------
        move : Move
        
        Returns
        -------
        None

    `opponent(self) ‑> checkers.game.Color`
    :   Get the opponent of the current Color
        
        Returns
        -------
        Color

    `undo(self) ‑> None`
    :   Cancels last move and recover previous state and board.
        
        Returns
        -------
        None

`GameState(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `BLACK_WON`
    :

    `TIE`
    :

    `UNFINISHED`
    :

    `WHITE_WON`
    :