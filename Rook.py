class Rook(Piece):
    
    @property
    def symbol(self):
        return "R"

    def can_move(self, board, frm, to):
        dr = abs(to[0]-frm[0])#מרחק שורות
        dc = abs(to[1]-frm[1])#מרחק עמודות
        return dc==0 or dr==0
            

    def path_is_clear(self, board, frm, to):
        if frm[0] == to[0]:
            step = 1 if to[1] > frm[1] else -1
            col = frm[1] + step
            while col != to[1]:
                if board[frm[0]][col] != ".":
                    return False
                col += step
            return True

        if frm[1] == to[1]:
            step = 1 if to[0] > frm[0] else -1
            row = frm[0] + step
            while row != to[0]:
                if board[row][frm[1]] != ".":
                    return False
                row += step
            return True

        return False