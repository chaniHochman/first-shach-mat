class Queen(Piece):

    @property
    def symbol(self):
        return "Q"

    def can_move(self, board, frm, to):
        dr = abs(to[0]-frm[0])#מרחק שורות
        dc = abs(to[1]-frm[1])#מרחק עמודות
        return (dc == 0 or dc == dr) and (dr == 0 or dr == dc)
    
      if dis_col==0 or dis_row==0:#אם כמו טורה
            if dis_col==0:
                if move_from[0]<move_to[0]:
                    i=move_from[0]+1
                    while i<move_to[0]:
                        if board[i][move_from[1]]!=".":
                            return False
                        i+=1
                else:
                    i=move_from[0]-1
                    while i>move_to[0]:
                        if board[i][move_from[1]]!=".":
                            return False
                        i-=1
            elif dis_row==0:
                if move_from[1]<move_to[1]:
                    i=move_from[1]+1
                    while i<move_to[1]:
                        if board[move_from[0]][i]!=".":
                            return False
                        i+=1
                else:
                    i=move_from[1]-1
                    while i>move_to[1]:
                        if board[move_from[0]][i]!=".":
                            return False
                        i-=1
            
        elif dis_col==dis_row:  #אם כמו רץ
            row_step = 1 if move_to[0] > move_from[0] else -1
            col_step = 1 if move_to[1] > move_from[1] else -1
            r = move_from[0] + row_step
            c = move_from[1] + col_step
            
            while (r, c) != (move_to[0], move_to[1]):
                if board[r][c] != ".":
                    return False
    
                r +=row_step
                c += col_step
            
        
        return True  