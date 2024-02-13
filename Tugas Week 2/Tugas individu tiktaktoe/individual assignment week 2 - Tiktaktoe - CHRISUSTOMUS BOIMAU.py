'''
Chrisustomus Boimau
IBDA
232300500
'''


class TicTacToe:

    move = 0
    def __init__(self):
        self._board = [[' ']*3 for j in range(3)]
        self._player = "X"

    def mark(self,i,j):
        TicTacToe.move += 1
        if not (0<=i<=2 and 0<=j<=2):
            raise ValueError('invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is alreaddy complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'


    def _is_win(self,mark):
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or mark == board[1][0] == board[1][1] == board[1][2] or mark == board[2][0] == board[2][1] == board[2][2] or mark == board[0][0] == board[1][0] == board[2][0] or mark == board[0][1] == board[1][1] == board[2][1] or mark == board[0][2] == board[1][2] == board[2][2] or mark == board[0][0] == board[1][1] == board[2][2] or mark == board[0][2] == board[1][1] == board[2][0])
    
    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
            return None
        
    def __str__(self):
        rows = ['|'.join(self._board[r])for r in range (3)]
        return '\n----\n'.join(rows)
    

game = TicTacToe()
while True:
    print(game._player, " its your turn")
    try:
        row = int(input("row = ")) - 1
        colloum = int(input("colloum = ")) - 1
    except:
        print("please input number betwen 1 and 3")
        continue
    game.mark(row,colloum)

    print(game)
    winner = game.winner()
    if TicTacToe.move == 9:
        print('Tie')
        break
    else:
        print(winner, 'wins')
        break
