from Piece import Piece


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
        if piece_from is None or piece_from == ".":
            return False

        piece_from_color = piece_from.color if hasattr(piece_from, "color") else piece_from[0]
        piece_to_color = piece_to.color if hasattr(piece_to, "color") else None

        # אם הכלי הוא שחור, בודק את כללי התנועה שלו
        if piece_from_color == "b":
            # שחור יכול ללכת צעד אחד ישר קדימה אם המשבצת ריקה
            if to[1] == frm[1] and to[0] == frm[0] + 1 and piece_to is None:
                return True

            # שחור יכול ללכת שני צעדים ישר מהעמדה ההתחלתית אם שתי המשבצות ריקות
            if to[1] == frm[1] and to[0] == frm[0] + 2 and frm[0] == 1 and piece_to is None and board[frm[0] + 1][frm[1]] is None:
                return True

            # שחור יכול לאכול אלכסונית קדימה אם יש כלי בצבע אחר ביעד
            if abs(to[1] - frm[1]) == 1 and to[0] == frm[0] + 1 and piece_to is not None and piece_to_color is not None and piece_to_color != piece_from_color:
                return True

        # אם הכלי הוא לבן, בודק את כללי התנועה שלו
        elif piece_from_color == "w":
            # לבן יכול ללכת צעד אחד ישר אחורה אם המשבצת ריקה
            if to[1] == frm[1] and to[0] == frm[0] - 1 and piece_to is None:
                return True

            # לבן יכול ללכת שני צעדים ישר מהעמדה ההתחלתית אם שתי המשבצות ריקות
            if to[1] == frm[1] and to[0] == frm[0] - 2 and frm[0] == len(board) - 2 and piece_to is None and board[frm[0] - 1][frm[1]] is None:
                return True

            # לבן יכול לאכול אלכסונית אחורה אם יש כלי בצבע אחר ביעד
            if abs(to[1] - frm[1]) == 1 and to[0] == frm[0] - 1 and piece_to is not None and piece_to_color is not None and piece_to_color != piece_from_color:
                return True

        # אם אף תנאי לא התקיים, התנועה לא חוקית
        return False
                    
    def path_is_clear(self, board, frm, to):
        dis_row = to[0] - frm[0]
        dis_col = to[1] - frm[1]
        piece_to = board[to[0]][to[1]]

        if dis_col != 0:
            return False

        if piece_to is not None and piece_to != ".":
            return False

        if abs(dis_row) == 2:
            middle_row = frm[0] + (1 if dis_row > 0 else -1)
            return board[middle_row][frm[1]] is None or board[middle_row][frm[1]] == "."

        return True