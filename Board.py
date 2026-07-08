from Piece import Piece
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight 
from Pawn import Pawn


class Board:
    def __init__(self, board_data):
        self.grid = []
        for row in board_data:
            new_row = []
            for cell in row:
                if cell == ".":
                    new_row.append(None)
                else:
                    color = cell[0]
                    piece_type = cell[1]

                    if piece_type == "K":
                        
                        new_row.append(King(color))
                    elif piece_type == "Q":
                        
                        new_row.append(Queen(color))
                    elif piece_type == "R":
                        
                        new_row.append(Rook(color))
                    elif piece_type == "B":
                        
                        new_row.append(Bishop(color))
                    elif piece_type == "N":
                       
                        new_row.append(Knight(color))
                    elif piece_type == "P":
                       
                        new_row.append(Pawn(color))
                    else:
                        new_row.append(None)
            self.grid.append(new_row)

        self.board = self.grid

    def rows(self):
        return len(self.grid)

    def cols(self):
        return len(self.grid[0]) if self.grid else 0

    def get(self, row, col):
        return self.grid[row][col]

    def set(self, row, col, piece):
        self.grid[row][col] = piece

    def __getitem__(self, index):
        return self.grid[index]

    def __len__(self):
        return len(self.grid)

    def move(self, frm, to):
        self.grid[to[0]][to[1]] = self.grid[frm[0]][frm[1]]
        self.grid[frm[0]][frm[1]] = None

    def print_board(self):
        for row in self.grid:
            display = []
            for cell in row:
                if cell is None:
                    display.append(".")
                else:
                    display.append(cell.to_string())
            print(" ".join(display))
