Module checkers.ai.random_ai
============================
This module contains class RandomAI

RandomAI just return random move from the moves that
were returned by the get_all_moves method of the Game.

This file can also be imported as module and contains the following
classes:

    * RandomAI - represents AI player that chooses moves randomly

Classes
-------

`RandomAI(size: int, color: checkers.game.Color)`
:   The class represents AI player that chooses moves randomly
    
    ...
    
    Attributes
    ----------
    _game : Game
        separate Game object that allows to get all possible moves
    color : Color
        color of AI player
    
    Methods
    -------
    make_move(opponent_move: Move | None = None) -> Move:
        takes last opponent's move if it was presented
        and returns randomly chosen move
    
    Creates separate Game object and writes color of AI player

    ### Methods

    `make_move(self, opponent_move: checkers.move.Move | None = None) ‑> checkers.move.Move`
    :   takes last opponent's move if it was presented
        and returns randomly chosen move
        
        Parameters
        ----------
        opponent_move : Move | None, optional
            last opponent's move if it was presented
        
        Returns
        -------
        Move
            Move is randomly chosen by AI