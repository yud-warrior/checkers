========
Сheckers
========
The package realizes `English chekers
<https://en.wikipedia.org/wiki/English_draughts>`_ game simulation.

Basic usage
-----------

Let's create a game with RandomAI:

.. code-block:: python
    
    from checkers.game import Game, GameState, Color
    from checkers.move import Move
    from checkers.ai.random_ai import RandomAI
    
    def main():
        size = 8
        game = Game(size)
        ai_color = Color.WHITE
        ai = RandomAI(size, ai_color)
        if ai_color == Color.BLACK:
            move = None
        while game.state == GameState.UNFINISHED:
            print(game.board)
            print('b:', game.black_count, 'w:', game.white_count)
            print(game.turn)
    
            if game.turn == ai_color:
                move = ai.make_move(move)
            else:
                moves = game.get_all_moves()
                for i, move in enumerate(moves):
                    print(i + 1, ':', move)
                print('Input number of the move for move:')
                try:
                    move_number = int(input().strip())
                except ValueError:
                    print('Wrong input. Number of the move must be int')
                try:
                    move = moves[move_number - 1]
                except IndexError:
                    print('Wrong move')
                    continue
            game.make_move(move)
        else:
            print(game.board)
            print(game.state)
    
    
    if __name__ == '__main__':
        main()

