class Game:

    def __init__(self):
        self.board = Board()
        self.selected = None
        self.moving = None

    def click(self,x,y):
        if moving is not None:
            return
        x = int(parts[1])
        y = int(parts[2])
        
        col = x // 100
        row = y // 100
        
        
        
        rows = len(board)
        cols = len(board[0])
        
        #בדיקה אם נמצא בתוך הלוח
        if row < 0 or row >= rows:
            return
        
        if col < 0 or col >= cols:
            return
        
        
        if selected is None: #אם אין בחירה עדיין
            if board[row][col] != ".":
                selected = (row, col)
        else:  #אם כבר בחרו
            piece1 = board[selected[0]][selected[1]]
            piece2 = board[row][col]
            if piece2 != "." and piece1[0] == piece2[0]:#האם זו אותה קבוצה?
                selected = (row, col)
            else:   #שלח בקשת מהלך
           
                move_from = selected
                move_to = (row, col)
                #בדיקה אם אפשר לעשות את הצעד הזה
                if if_possible(move_from,move_to,board):
                    if if_the_way_is_empty(move_from,move_to,board):
                        if if_same_color(move_from,move_to,board):
                
                            piece = board[move_from[0]][move_from[1]]
                            distance = max(
                                abs(move_to[0] - move_from[0]),
                                abs(move_to[1] - move_from[1])
                            )
                            
                            moving = {
                                "piece": piece,
                                "from": move_from,
                                "to": move_to,
                                "time_left": distance * 1000
                            }
                            # board[move_from[0]][move_from[1]] = "."
                            # board[move_to[0]][move_to[1]] = piece
                        
                            selected = None

    def wait(self,ms):
        ms = int(parts[1])
        
        if moving is not None:
            moving["time_left"] -= ms
        
            if moving["time_left"] <= 0:
                fr = moving["from"]
                to = moving["to"]
                #עשית צעד
                # if both_kings_exist(board):
                board[fr[0]][fr[1]] = "."
                board[to[0]][to[1]] = moving["piece"]
        
                moving = None
                piece = board[to[0]][to[1]]
                #הוספה של תרגיל 10
                #אם חייל הגיע לשורה האחרונה הופכים אותו למלכה
                if piece == "wP" and to[0] == 0:
                    board[to[0]][to[1]] = "wQ"
                
                elif piece == "bP" and to[0] == len(board) - 1:
                    board[to[0]][to[1]] = "bQ"
                        
                        

    def print_board(self):
        for row in board:
            print(" ".join(row))  



    #קלט
board,commands=read_board()

selected = None#האם נבחר כלי
moving = None#האם הכלי יכול לזוז
for line in commands:
    
    parts = line.split()

    command = parts[0]


    #לחיצה
    if command == "click":
       
    elif parts[0] == "wait":
       
    elif parts[0] == "print" and parts[1] == "board":
        
            

#במקום
#if_possible(...)
#piece = board.get(r,c)

#piece.can_move(board, frm, to)


# במקום
# if_same_color(...)

# target = board.get(r,c)

# if target is None:
#     ...

# elif target.color == piece.color:
#     ...