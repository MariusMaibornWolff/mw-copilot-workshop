import unittest

from game import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_a_move_changes_the_board(self):
        # arrange
        game = TicTacToe()
        game.current_player = 'X'
        # act
        game.move(0, 1)
        # assert
        self.assertEqual('X', game.board[0][1])

    def test_a_move_changes_the_player(self):
        # arrange
        game = TicTacToe()
        game.current_player = 'X'
        # act
        game.move(0, 1)
        # assert
        self.assertEqual('O', game.current_player)



if __name__ == '__main__':
    unittest.main()
