from asyncio import run
import sys
import re

from board import Board

class Game:

    def __init__(self):
        
        self.selected = None
        self.moving = None
        board,commands=read_board()
        self.board = Board(board)
        self.do_commands(commands)


    def read_board():
        lines=sys.stdin.read().splitlines()
        
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
                board.append(line.split())#קריאת שורה במטריצה
            if reading_commands:
                commands.append(line)#קריאת פקודה
        
        #בדיקת רוחב שורות
        if len(board) == 0:
            print("ERROR EMPTY_BOARD")
            sys.exit()
        width = len(board[0])
        
        for row in board:
            if len(row) != width:
                print("ERROR ROW_WIDTH_MISMATCH")
                sys.exit()
        
        valid = {'.'}
        
        for color in ('w', 'b'):
            for piece in ('K', 'Q', 'R', 'B', 'N', 'P'):
                valid.add(color + piece)
        #valid-רשימת כל סוגי החיילים
        
        #בדיקה אם יש חייל שלא קיים הסוג שלו
        for row in board:
            for token in row:
                if token not in valid:
                    print("ERROR UNKNOWN_TOKEN")
                    sys.exit()
    
        board_game=Board(board)
        commands_game=commands(commands)
        return(board_game,commands_game)

    def click(self,x,y):
        if self.moving is not None:
            return
        # x = int(parts[1])
        # y = int(parts[2])
        
        col = x // 100
        row = y // 100
        
        # rows = len(board)
        # cols = len(board[0])
        
        #בדיקה אם נמצא בתוך הלוח
        if row < 0 or row >= self.board.rows():
            return
        
        if col < 0 or col >= self.board.cols():
            return
        
        
        if selected is None: #אם אין בחירה עדיין
            piece = self.board.get(row, col)

            if piece is not None:
                self.selected = (row, col)

            return
          #אם כבר בחרו

        frm = self.selected
        to = (row, col)

        piece = self.board.get(frm[0], frm[1])
        target = self.board.get(to[0], to[1])

        # לחיצה על כלי מאותו צבע -> מחליפים בחירה
        if target is not None and piece.same_color(target):
            self.selected = to
            return

        if not piece.can_move(self.board, frm, to):
            self.selected = None
            return

        if not piece.path_is_clear(self.board, frm, to):
            self.selected = None
            return

        distance = max(
            abs(to[0] - frm[0]),
            abs(to[1] - frm[1])
        )

        self.moving = {
            "piece": piece,
            "from": frm,
            "to": to,
            "time_left": distance * 1000
        }

        self.selected = None

    def wait(self, ms):
        # ממיר את הזמן למספר שלם כדי שניתן לחסר ממנו בצורה תקינה
        ms = int(ms)

        # בודק אם יש תנועה פעילה שממתינה לסיום הזמן שלה
        if self.moving is not None:
            # מוריד את הזמן שנותר לתנועה
            self.moving["time_left"] -= ms

            # אם הזמן נגמר, מבצע את התנועה בפועל
            if self.moving["time_left"] <= 0:
                # לוקח את מיקום ההתחלה של התנועה
                fr = self.moving["from"]
                # לוקח את מיקום הסיום של התנועה
                to = self.moving["to"]

                # בודק אם הלוח משתמש בשיטות get/set של אובייקט Board
                if hasattr(self.board, "get") and hasattr(self.board, "set"):
                    # לוקח את הכלי מהמקום ההתחלתי
                    piece = self.board.get(fr[0], fr[1])
                    # מנקה את המשבצת ההתחלתית
                    self.board.set(fr[0], fr[1], None)
                    # מכניס את הכלי למשבצת הסופית
                    self.board.set(to[0], to[1], piece)
                    # לוקח את הכלי החדש שנמצא ביעד
                    moved_piece = self.board.get(to[0], to[1])
                else:
                    # לוקח את הכלי מהמקום ההתחלתי אם הלוח הוא רשימת רשימות
                    piece = self.board[fr[0]][fr[1]]
                    # מנקה את המשבצת ההתחלתית
                    self.board[fr[0]][fr[1]] = None
                    # מכניס את הכלי למשבצת הסופית
                    self.board[to[0]][to[1]] = piece
                    # לוקח את הכלי החדש שנמצא ביעד
                    moved_piece = self.board[to[0]][to[1]]

                # מסיר את התנועה הפעילה מהמערכת לאחר ביצוע הצעד
                self.moving = None

                # קובע את הקוד של הכלי שנמצא עכשיו ביעד כדי לבדוק אם צריך לקדם אותו
                piece_code = moved_piece.to_string() if hasattr(moved_piece, "to_string") else moved_piece

                # אם חייל לבן הגיע לקצה העליון, הופך אותו למלכה
                if piece_code == "wP" and to[0] == 0:
                    self.board.set(to[0], to[1], "wQ") if hasattr(self.board, "set") else self.board.__setitem__(to[0], to[1], "wQ")

                # אם חייל שחור הגיע לקצה התחתון, הופך אותו למלכה
                elif piece_code == "bP" and to[0] == len(self.board) - 1:
                    self.board.set(to[0], to[1], "bQ") if hasattr(self.board, "set") else self.board.__setitem__(to[0], to[1], "bQ")

    def print_board(self):
        self.board.print_board() 

    def do_commands(self, commands):
        for line in commands:
            parts = line.split()
            command = parts[0]

            if command == "click":
                x = int(parts[1])
                y = int(parts[2])
                self.click(x, y)
            elif command == "wait":
                ms = int(parts[1])
                self.wait(ms)
            elif command == "print" and parts[1] == "board":
                self.print_board()




        
