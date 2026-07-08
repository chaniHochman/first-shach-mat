import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Board import Board
from Game import Game
from King import King
from Pawn import Pawn
from Queen import Queen


class ChessProjectTests(unittest.TestCase):
    def make_board(self, size=8):
        return Board([["." for _ in range(size)] for _ in range(size)])

    def test_board_initializes_piece_objects(self):
        board_data = [["wK", "."], [".", "bP"]]
        board = Board(board_data)

        self.assertIsInstance(board.get(0, 0), King)
        self.assertEqual(board.get(0, 0).to_string(), "wK")
        self.assertIsNone(board.get(0, 1))
        self.assertIsInstance(board.get(1, 1), Pawn)

    def test_pawn_can_move_one_step_forward(self):
        board = self.make_board()
        board_data = board.grid
        board_data[6][3] = "wP"
        board = Board([["." for _ in range(8)] for _ in range(8)])
        board.grid[6][3] = Pawn("w")

        pawn = board.get(6, 3)
        self.assertTrue(pawn.can_move(board, (6, 3), (5, 3)))

    def test_pawn_can_capture_diagonally(self):
        board = self.make_board()
        board.grid[6][3] = Pawn("w")
        board.grid[5][2] = Pawn("b")

        pawn = board.get(6, 3)
        self.assertTrue(pawn.can_move(board, (6, 3), (5, 2)))

    def test_queen_path_is_clear_for_straight_and_diagonal_moves(self):
        board = self.make_board()
        board.grid[3][3] = Queen("w")

        queen = board.get(3, 3)
        self.assertTrue(queen.path_is_clear(board, (3, 3), (3, 6)))
        self.assertTrue(queen.path_is_clear(board, (3, 3), (6, 6)))

    def test_queen_path_is_blocked(self):
        board = self.make_board()
        board.grid[3][3] = Queen("w")
        board.grid[3][4] = Pawn("b")

        queen = board.get(3, 3)
        self.assertFalse(queen.path_is_clear(board, (3, 3), (3, 6)))

    def test_game_wait_promotes_pawn(self):
        board = self.make_board()
        board.grid[6][0] = Pawn("w")

        game = Game.__new__(Game)
        game.board = board
        game.moving = {"from": (6, 0), "to": (0, 0), "time_left": 1}

        game.wait(1)

        self.assertEqual(game.board.get(0, 0), "wQ")


if __name__ == "__main__":
    unittest.main()
