from Piece import Piece


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

   




    
    
    # הדפסה
    def print_board(self):
        for row in board:
            print(" ".join(row))
    

    class Board:

    