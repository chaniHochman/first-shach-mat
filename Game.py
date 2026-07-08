import sys

from Board import Board


class Game:
    def __init__(self):
        self.selected = None
        self.moving = None
        board_data, commands = self.read_board()
        self.board = Board(board_data)
        self.do_commands(commands)

    @staticmethod
    def read_board():
        lines = sys.stdin.read().splitlines()

        reading_commands = False
        commands = []
        board = []
        reading = False

        for line in lines:
            if line.strip() == "Board:":
                reading = True
                continue
            if line.strip() == "Commands:":
                reading = False
                reading_commands = True
                continue
            if reading and line.strip():
                board.append(line.split())
            if reading_commands:
                commands.append(line)

        if len(board) == 0:
            print("ERROR EMPTY_BOARD")
            sys.exit()

        width = len(board[0])
        for row in board:
            if len(row) != width:
                print("ERROR ROW_WIDTH_MISMATCH")
                sys.exit()

        valid = {"."}
        for color in ("w", "b"):
            for piece in ("K", "Q", "R", "B", "N", "P"):
                valid.add(color + piece)

        for row in board:
            for token in row:
                if token not in valid:
                    print("ERROR UNKNOWN_TOKEN")
                    sys.exit()

        return board, commands

    def click(self, x, y):
        if self.moving is not None:
            return

        col = x // 100
        row = y // 100

        if row < 0 or row >= self.board.rows():
            return
        if col < 0 or col >= self.board.cols():
            return

        if self.selected is None:
            piece = self.board.get(row, col)
            if piece is not None:
                self.selected = (row, col)
            return

        frm = self.selected
        to = (row, col)

        piece = self.board.get(frm[0], frm[1])
        target = self.board.get(to[0], to[1])

        if target is not None and piece.same_color(target):
            self.selected = to
            return

        if not piece.can_move(self.board, frm, to):
            self.selected = None
            return

        if not piece.path_is_clear(self.board, frm, to):
            self.selected = None
            return

        distance = max(abs(to[0] - frm[0]), abs(to[1] - frm[1]))
        self.moving = {
            "piece": piece,
            "from": frm,
            "to": to,
            "time_left": distance * 1000,
        }
        self.selected = None

    def wait(self, ms):
        ms = int(ms)

        if self.moving is not None:
            self.moving["time_left"] -= ms

            if self.moving["time_left"] <= 0:
                fr = self.moving["from"]
                to = self.moving["to"]

                piece = self.board.get(fr[0], fr[1])
                self.board.set(fr[0], fr[1], None)
                self.board.set(to[0], to[1], piece)
                moved_piece = self.board.get(to[0], to[1])

                self.moving = None
                #בדיקה אם חייל הגיע לסוף הלוח והפיכתו למלכה
                piece_code = moved_piece.to_string() if hasattr(moved_piece, "to_string") else moved_piece
                if piece_code == "wP" and to[0] == 0:
                    self.board.set(to[0], to[1], "wQ")
                elif piece_code == "bP" and to[0] == len(self.board) - 1:
                    self.board.set(to[0], to[1], "bQ")

    def print_board(self):
        self.board.print_board()

    def do_commands(self, commands):
        for line in commands:
            parts = line.split()
            if not parts:
                continue
            command = parts[0]

            if command == "click":
                x = int(parts[1])
                y = int(parts[2])
                self.click(x, y)
            elif command == "wait":
                ms = int(parts[1])
                self.wait(ms)
            elif command == "print" and len(parts) > 1 and parts[1] == "board":
                self.print_board()

