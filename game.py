class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'

    def move(self, row, col):
        # TODO implement move logic
        pass

    def get_winner(self):
        # TODO implement winner logic
        pass

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

class TicTacToeUI:
    def __init__(self, game):
        self.game = game

    def get_move_input(self):
        return int(input("Enter the row for your move (0-2): ")), int(input("Enter the column for your move (0-2): "))

    def print_board(self):
        board = self.game.get_board()
        print('\n' + ' ' * 8 + ' 0   1   2')
        print(' ' * 5 + '-' * 17)
        for i, row in enumerate(board):
            print(' ' * 5 + str(i) + ' | ' + ' | '.join(row) + ' | ')
            print(' ' * 5 + '-' * 17)
        print()

    def play(self):
        while True: # TODO implement game loop that checks for winner
            print(f"\nPlayer {self.game.get_current_player()}'s turn\n")
            self.print_board()
            row, col = self.get_move_input()
            if not self.game.move(row, col):
                print("Invalid move, try again.")

if __name__ == '__main__':
    game = TicTacToe()
    ui = TicTacToeUI(game)
    ui.play()
