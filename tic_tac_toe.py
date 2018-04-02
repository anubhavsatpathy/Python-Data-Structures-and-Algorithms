class TicTacToe:

    def __init__(self):
        """
        Constructor for the tic-tac-toe game object
        1. Initializes the game state representation as a list of lists of characters
            ' ' = Empty
            'O' = Zeros
            'X' = Crosses
        """

        self._board = [[' ']*3 for j in range(3)]
        self._player = 'X'
        self._is_complete = False

    def mark(self,i,j):
        """
        Method that marks a board position with a players symbol
        :param i: Row number - should be in the closed range [0,2]
        :param j: Column number -should be in the closed range [0,2]
        :return: void - modifies the game state - self._board
        """
        if not(0<=i<=2 and 0<=j<=2):

            raise ValueError("Invalid Board Position")

        if self._board[i][j] != ' ':

            raise ValueError("Board Position Occupied")

        if self._is_complete:

            raise ValueError("Game is already complete")

        self._board[i][j] = self._player

        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

        if self.is_winner('X'):
            print("Winner ---- X")
            self._is_complete = True
        if self.is_winner('O'):
            print("Winner ---- O")
            self._is_complete = True

    def is_complete(self):

        return self.is_winner('X') or self.is_winner('O')

    def is_winner(self, sym):

        for i in range(3):
            if sym == self._board[i][0] == self._board[i][1] == self._board[i][2]:
                return True
            else:
                if sym == self._board[0][i] == self._board[1][i] == self._board[2][i]:
                    return True

        if sym == self._board[0][0] == self._board[1][1] == self._board[2][2] or sym == self._board[0][2] == self._board[1][1] == self._board[2][0]:
            return True
        else:
            return False

    def __str__(self):

        rows = [" | ".join(self._board[r]) for r in range(3)]
        return "\n-----------\n".join(rows)

if __name__ == "__main__":
    game = TicTacToe()
    game.mark(0, 1)
    print(str(game) + "\n\n___________________\n")
    game.mark(0, 0)
    print(str(game) + "\n\n___________________\n")
    game.mark(0, 2)
    print(str(game) + "\n\n___________________\n")
    game.mark(1, 1)
    print(str(game) + "\n\n___________________\n")
    game.mark(1, 2)
    print(str(game) + "\n\n___________________\n")
    game.mark(2, 2)
    print(str(game) + "\n\n___________________\n")
    #game.mark(2,0)
    #print(str(game) + "\n\n___________________\n")
