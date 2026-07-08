class Board:
    def __init__(self, board_data):
        self.board = board_data

        for row in board_data:
            new_row = []
            for cell in row:
                if cell == ".":
                    new_row.append(None)
                else:
                    color = cell[0]
                    piece_type = cell[1]
                    new_row.append(Piece(piece_type, color))
            self.board.append(new_row)



import sys
import re
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
   
    board_game=board(board)
    commands_game=commands(commands)
    return(board_game,commands_game)
    
    
    # הדפסה
    def print_board(self):
        for row in board:
            print(" ".join(row))
    

    class Board:

    def __init__(self):
        self.grid = []

    def rows(self):
        return len(self.grid)

    def cols(self):
        return len(self.grid[0])

    def get(self,row,col):
        return self.grid[row][col]

    def set(self,row,col,piece):
        self.grid[row][col]=piece

    def move(self,frm,to):
        self.grid[to[0]][to[1]]=self.grid[frm[0]][frm[1]]
        self.grid[frm[0]][frm[1]]=None