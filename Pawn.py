class Pawn(Piece):#חייל פשוט

    @property
    def symbol(self):
        return "P"

    def can_move(self, board, frm, to):
        # אם ההתחלה והסוף זהים, אין תנועה חוקית
        if frm == to:
            return False

        # לוקח את הכלי מהשורה/עמודה של המקור
        piece_from = board[frm[0]][frm[1]]
        # לוקח את הכלי מהיעד, אם קיים
        piece_to = board[to[0]][to[1]]

        # אם אין כלי במקור, התנועה לא חוקית
        if piece_from == ".":
            return False

        # אם הכלי הוא שחור, בודק את כללי התנועה שלו
        if piece_from[0] == "b":
            # שחור יכול ללכת צעד אחד ישר קדימה אם המשבצת ריקה
            if to[1] == frm[1] and to[0] == frm[0] + 1 and piece_to == ".":
                return True

            # שחור יכול ללכת שני צעדים ישר מהעמדה ההתחלתית אם שתי המשבצות ריקות
            if to[1] == frm[1] and to[0] == frm[0] + 2 and frm[0] == 1 and piece_to == "." and board[frm[0] + 1][frm[1]] == ".":
                return True

            # שחור יכול לאכול אלכסונית קדימה אם יש כלי בצבע אחר ביעד
            if abs(to[1] - frm[1]) == 1 and to[0] == frm[0] + 1 and piece_to != "." and piece_to[0] != piece_from[0]:
                return True

        # אם הכלי הוא לבן, בודק את כללי התנועה שלו
        elif piece_from[0] == "w":
            # לבן יכול ללכת צעד אחד ישר אחורה אם המשבצת ריקה
            if to[1] == frm[1] and to[0] == frm[0] - 1 and piece_to == ".":
                return True

            # לבן יכול ללכת שני צעדים ישר מהעמדה ההתחלתית אם שתי המשבצות ריקות
            if to[1] == frm[1] and to[0] == frm[0] - 2 and frm[0] == len(board) - 2 and piece_to == "." and board[frm[0] - 1][frm[1]] == ".":
                return True

            # לבן יכול לאכול אלכסונית אחורה אם יש כלי בצבע אחר ביעד
            if abs(to[1] - frm[1]) == 1 and to[0] == frm[0] - 1 and piece_to != "." and piece_to[0] != piece_from[0]:
                return True

        # אם אף תנאי לא התקיים, התנועה לא חוקית
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