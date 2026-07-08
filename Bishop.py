   
from Piece import Piece


class Bishop(Piece):
    @property
    def symbol(self):
        return "B"

    def can_move(self, board, frm, to):
        dr = abs(to[0]-frm[0])#מרחק שורות
        dc = abs(to[1]-frm[1])#מרחק עמודות
        return dc==dr
            

    def path_is_clear(self, board, frm, to):
        row_step = 1 if to[0] > frm[0] else -1
        col_step = 1 if to[1] > frm[1] else -1
        r = frm[0] + row_step
        c = frm[1] + col_step
        
        while (r, c) != (to[0], to[1]):
            if board[r][c] != ".":
                return False

            r +=row_step
            c += col_step
        return True