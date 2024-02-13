import random


class TicTacToe:
    """Management of a Tic-Tac Toe game (does not do strategy)."""

    def __init__(self):
        """Start a new game."""
        self._board = [[''] * 3 for _ in range(3)]
        self._player = 'X'
        self._bot = 'O'

    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for the next player's turn."""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != '':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        self._player, self._bot = self._bot, self._player  # Swap player and bot

    def _is_win(self, mark):
        """Check if the given mark has won the game."""
        board = self._board

        # Pengecekan Row
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] == mark:
                return True

        # Pengecekan columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == mark:
                return True

        # Pengecekan diagonals
        if board[0][0] == board[1][1] == board[2][2] == mark:
            return True
        if board[0][2] == board[1][1] == board[2][0] == mark:
            return True

        return False

    def winner(self):
        """Return the mark of the winning player, or None to indicate a tie."""
        for mark in ['X', 'O']:
            if self._is_win(mark):
                return mark
        return None

    def is_board_full(self):
        """Check if the game board is full."""
        for row in range(3):
            for col in range(3):
                if self._board[row][col] == '':
                    return False
        return True

    def print_board(self):
        """Print the current game board."""
        for row in range(3):
            print('|'.join(self._board[row]))
            if row < 2:
                print('-----')

    def play(self):
        """Start the game and play until there's a winner or a tie."""
        print("Let's play Tic Tac Toe!")
        print("You are 'X' and the bot is 'O'.")
        print("Enter row and column numbers to make a move.")
        print("Rows and columns are 0-indexed.")

        while True:
            self.print_board()

            # Giiran Pemain
            while True:
                try:
                    row = int(input("Enter the row number: "))
                    col = int(input("Enter the column number: "))
                    self.mark(row, col)
                    break
                except (ValueError, IndexError, ValueError) as e:
                    print(f"Invalid move: {e}")

            # Check and Recheck
            if self.winner() == 'X':
                self.print_board()
                print("Congratulations! You won!")
                break
            elif self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            # Giliran Bot
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                try:
                    self.mark(row, col)
                    break
                except ValueError:
                    continue

            # Check dan recheck akhir game
            if self.winner() == 'O':
                self.print_board()
                print("The bot wins!")
                break
            elif self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break


# Mainkan
if __name__ == '__main__':
    game = TicTacToe()
    game.play()