class Pawn(Piece):

    @property
    def symbol(self):
        return "P"

    def can_move(self, board, frm, to):
        if frm == to:
            return False

        piece_from = board[frm[0]][frm[1]]
        piece_to = board[to[0]][to[1]]

        if piece_from == ".":
            return False

        if piece_from[0] == "b":
            if to[1] == frm[1] and to[0] == frm[0] + 1 and piece_to == ".":
                return True

            if to[1] == frm[1] and to[0] == frm[0] + 2 and frm[0] == 1 and piece_to == "." and board[frm[0] + 1][frm[1]] == ".":
                return True

            if abs(to[1] - frm[1]) == 1 and to[0] == frm[0] + 1 and piece_to != "." and piece_to[0] != piece_from[0]:
                return True

        elif piece_from[0] == "w":
            if to[1] == frm[1] and to[0] == frm[0] - 1 and piece_to == ".":
                return True

            if to[1] == frm[1] and to[0] == frm[0] - 2 and frm[0] == len(board) - 2 and piece_to == "." and board[frm[0] - 1][frm[1]] == ".":
                return True

            if abs(to[1] - frm[1]) == 1 and to[0] == frm[0] - 1 and piece_to != "." and piece_to[0] != piece_from[0]:
                return True

        return False
                    
    def path_is_clear(self, board, frm, to):
        dis_row = to[0] - frm[0]
        dis_col = to[1] - frm[1]
        piece_from = board[frm[0]][frm[1]]
        piece_to = board[to[0]][to[1]]
        if piece_from[0]=="b":
            if dis_row==2 and dis_col==0:#מרחק שתי צעדים
                if move_from[0]==0:#נמצא בשורה הראשונה
                    # if move_from[1]==move_to[1]:#אם נמצאים באותו טור
                    if  piece_to==".":
                        return True
                        
        elif piece_from[0]=="w":
            if dis_row==-2 and dis_col==0:#מרחק שתי צעדים
                if move_from[0]==len(board)-1:#נמצא בשורה הראשונה
                    # if move_from[1]==move_to[1]:#אם נמצאים באותו טור
                    if piece_to==".":
                        return True
        return False