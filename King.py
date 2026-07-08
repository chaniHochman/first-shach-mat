class King(Piece):

    @property
    def symbol(self):
        return "K"

    def can_move(self, board, frm, to):
        dr = abs(to[0]-frm[0])
        dc = abs(to[1]-frm[1])
        return dr <= 1 and dc <= 1 and (dr or dc)

    def path_is_clear(self, board, frm, to):
        return True