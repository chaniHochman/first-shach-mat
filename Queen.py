class Queen(Piece):
 
    @property
    def symbol(self):
        return "Q"
   
    
    def can_move(self, board, frm, to):
        if frm == to:
            return False

        dr = abs(to[0] - frm[0])
        dc = abs(to[1] - frm[1])

        return (dr == 0 or dc == 0 or dr == dc)

    def path_is_clear(self, board, frm, to):
        if frm == to:
            return True

        if frm[0] == to[0]:#אם כמו טורה
            step = 1 if to[1] > frm[1] else -1
            col = frm[1] + step
            while col != to[1]:
                if board[frm[0]][col] != ".":
                    return False
                col += step
            return True

        if frm[1] == to[1]:#אם כמו טורה
            step = 1 if to[0] > frm[0] else -1
            row = frm[0] + step
            while row != to[0]:
                if board[row][frm[1]] != ".":
                    return False
                row += step
            return True

        if abs(to[0] - frm[0]) == abs(to[1] - frm[1]):#אם כמו רץ
            row_step = 1 if to[0] > frm[0] else -1
            col_step = 1 if to[1] > frm[1] else -1
            row = frm[0] + row_step
            col = frm[1] + col_step
            while (row, col) != (to[0], to[1]):
                if board[row][col] != ".":
                    return False
                row += row_step
                col += col_step
            return True

        return False
