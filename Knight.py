class Knight(Piece):
    @property
    def symbol(self):
        return "N"

    def can_move(self, board, frm, to):
        dr = abs(to[0]-frm[0])#מרחק שורות
        dc = abs(to[1]-frm[1])#מרחק עמודות
        return (dc == 2 and dr == 1) or (dc == 1 and dr == 2)

    def path_is_clear(self, board, frm, to):
        return True