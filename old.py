# import sys
# import re

# def read_board():
#     lines=sys.stdin.read().splitlines()
    
#     reading_commands = False
#     commands = []
#     board = []
#     reading = False
    
#     for line in lines:
#         if line.strip() == "Board:":
#             reading = True
#             continue
#         if line.strip() == "Commands:":
#             reading = False
#             reading_commands = True
#             continue
#         if reading and line.strip():
#             board.append(line.split())
#         if reading_commands:
#             commands.append(line)
    
#     #בדיקת רוחב שורות
#     if len(board) == 0:
#         print("ERROR EMPTY_BOARD")
#         sys.exit()
#     width = len(board[0])
    
#     for row in board:
#         if len(row) != width:
#             print("ERROR ROW_WIDTH_MISMATCH")
#             sys.exit()
    
#     valid = {'.'}
    
#     for color in ('w', 'b'):
#         for piece in ('K', 'Q', 'R', 'B', 'N', 'P'):
#             valid.add(color + piece)
    
#     for row in board:
#         for token in row:
#             if token not in valid:
#                 print("ERROR UNKNOWN_TOKEN")
#                 sys.exit()
#     #הדפסה
#     # for row in board:
#     #     print(" ".join(row))
#     return board,commands
#הוספה של תרגיל 3
# def if_possible(move_from,move_to,board):
#     piece = board[move_from[0]][move_from[1]]
#     #piece[0]=צבע  piece[1]=סוג הכלי
#     #יקת המרחק בין הנקודה הקודמם לנקודה עכשיו
#     dis_row = abs(move_to[0] - move_from[0])
#     dis_col = abs(move_to[1] - move_from[1])
    
    # if piece[1]=="K": #מלך
    #     if dis_row <= 1 and dis_col <= 1 and (dis_row != 0 or dis_col != 0):
    #         return True
    # elif piece[1]=="R": #צריח-טורה
    #     if dis_col==0 or dis_row==0:
    #         return True
    # elif piece[1]=="B": #רץ
    #     if dis_col==dis_row:
    #         return True
    # elif piece[1]=="Q": #מלכה
    #     if dis_col==0 or dis_row==0 or dis_col==dis_row:
    #         return True
    # elif piece[1]=="N": #סוס-פרש
    #     if (dis_col==1 and dis_row==2) or (dis_col==2 and dis_row==1):
    #         return True
    # elif piece[1]=="P":#חייל
        # dis_row = move_to[0] - move_from[0]
        # dis_col = move_to[1] - move_from[1]
        # piece_from = board[move_from[0]][move_from[1]]
        # piece_to = board[move_to[0]][move_to[1]]
        # if piece[0]=="b":
        #     if dis_row==1:
        #         if dis_col==0 and piece_to == ".":
        #             return True
        #         elif abs(dis_col)==1:
        #             if piece_to != "." and piece_to[0]!=piece_from[0]:#אם הם באותו צבע
        #                 return True
        #     #הוספה של תרגיל 10
        #     elif dis_row==2 and dis_col==0:#מרחק שתי צעדים
        #         if move_from[0]==0:#נמצא בשורה הראשונה
        #             # if move_from[1]==move_to[1]:#אם נמצאים באותו טור
        #             if  piece_to==".":
        #                 return True
                        
        # elif piece[0]=="w":
        #     if dis_row==-1:
        #         if dis_col==0 and piece_to == ".":
        #             return True
        #         elif abs(dis_col)==1:
        #             if piece_to != "." and piece_to[0]!=piece_from[0]:#אם הם באותו צבע
        #                 return True
        #                 #הוספה של תרגיל 10
        #     elif dis_row==-2 and dis_col==0:#מרחק שתי צעדים
        #         if move_from[0]==len(board)-1:#נמצא בשורה הראשונה
        #             # if move_from[1]==move_to[1]:#אם נמצאים באותו טור
        #             if piece_to==".":
        #                 return True
        
    # return False

#הוספה של תרגיל 4
# def if_the_way_is_empty(move_from,move_to,board):
#     piece = board[move_from[0]][move_from[1]]
#     #piece[0]=צבע  piece[1]=סוג הכלי
#     #יקת המרחק בין הנקודה הקודמם לנקודה עכשיו
#     dis_row = abs(move_to[0] - move_from[0])
#     dis_col = abs(move_to[1] - move_from[1])
    
    # if piece[1]=="K": #מלך
        
    #     return True
    # elif piece[1]=="R": #צריח-טורה
        # if dis_col==0:
        #     if move_from[0]<move_to[0]:
        #         i=move_from[0]+1
        #         while i<move_to[0]:
        #             if board[i][move_from[1]]!=".":
        #                 return False
        #             i+=1
        #     else:
        #         i=move_from[0]-1
        #         while i>move_to[0]:
        #             if board[i][move_from[1]]!=".":
        #                 return False
        #             i-=1
        # elif dis_row==0:
        #     if move_from[1]<move_to[1]:
        #         i=move_from[1]+1
        #         while i<move_to[1]:
        #             if board[move_from[0]][i]!=".":
        #                 return False
        #             i+=1
        #     else:
        #         i=move_from[1]-1
        #         while i>move_to[1]:
        #             if board[move_from[0]][i]!=".":
        #                 return False
        #             i-=1
        # return True
    # elif piece[1]=="B": #רץ
        # row_step = 1 if move_to[0] > move_from[0] else -1
        # col_step = 1 if move_to[1] > move_from[1] else -1
        # r = move_from[0] + row_step
        # c = move_from[1] + col_step
        
        # while (r, c) != (move_to[0], move_to[1]):
        #     if board[r][c] != ".":
        #         return False

        #     r +=row_step
        #     c += col_step
        # return True
    # elif piece[1]=="Q": #מלכה
        # if dis_col==0 or dis_row==0:#אם כמו טורה
        #     if dis_col==0:
        #         if move_from[0]<move_to[0]:
        #             i=move_from[0]+1
        #             while i<move_to[0]:
        #                 if board[i][move_from[1]]!=".":
        #                     return False
        #                 i+=1
        #         else:
        #             i=move_from[0]-1
        #             while i>move_to[0]:
        #                 if board[i][move_from[1]]!=".":
        #                     return False
        #                 i-=1
        #     elif dis_row==0:
        #         if move_from[1]<move_to[1]:
        #             i=move_from[1]+1
        #             while i<move_to[1]:
        #                 if board[move_from[0]][i]!=".":
        #                     return False
        #                 i+=1
        #         else:
        #             i=move_from[1]-1
        #             while i>move_to[1]:
        #                 if board[move_from[0]][i]!=".":
        #                     return False
        #                 i-=1
            
        # elif dis_col==dis_row:  #אם כמו רץ
        #     row_step = 1 if move_to[0] > move_from[0] else -1
        #     col_step = 1 if move_to[1] > move_from[1] else -1
        #     r = move_from[0] + row_step
        #     c = move_from[1] + col_step
            
        #     while (r, c) != (move_to[0], move_to[1]):
        #         if board[r][c] != ".":
        #             return False
    
        #         r +=row_step
        #         c += col_step
            
        
        # return True    
    # elif piece[1]=="N": #סוס-פרש
    #     return True
    # elif piece[1] == "P":#חייל
    #     if abs(move_to[0] - move_from[0]) != 2:
    #         return True
            
    #     if piece[0]=="b":
    #         return (board[move_from[0] + 1][move_from[1]]=="." and board[move_to[0]][move_to[1]] == ".")
                
    #     else:
    #         return (board[move_from[0] - 1][move_from[1]]=="." and board[move_to[0]][move_to[1]] == ".")
               
    # return False 
# #בדיקה אם הם באותו צבע    
# def if_same_color(move_from,move_to,board):
#     piece_from = board[move_from[0]][move_from[1]]
#     piece_to = board[move_to[0]][move_to[1]]
#     if piece_to == ".":
#         return True
#     if piece_to[0]==piece_from[0]:#אם הם באותו צבע
#         return False
#     return True
# #הוספה של תרגיל אם עדיין יש את שתי המלכים על הלוח 9
# def both_kings_exist(board):
#     white = False
#     black = False

#     for row in board:
#         for cell in row:
#             if cell == "wK":
#                 white = True
#             elif cell == "bK":
#                 black = True

#     if white and black:
#         return True

#     return False
#קלט
# board,commands=read_board()

# selected = None#האם נבחר כלי
# moving = None#האם הכלי יכול לזוז
# for line in commands:
    
#     parts = line.split()

#     command = parts[0]


    # #לחיצה
    # if command == "click":
    #     if moving is not None:
    #         continue
    #     x = int(parts[1])
    #     y = int(parts[2])
        
    #     col = x // 100
    #     row = y // 100
        
        
        
    #     rows = len(board)
    #     cols = len(board[0])
        
    #     #בדיקה אם נמצא בתוך הלוח
    #     if row < 0 or row >= rows:
    #         continue
        
    #     if col < 0 or col >= cols:
    #         continue
        
        
    #     if selected is None: #אם אין בחירה עדיין
    #         if board[row][col] != ".":
    #             selected = (row, col)
    #     else:  #אם כבר בחרו
    #         piece1 = board[selected[0]][selected[1]]
    #         piece2 = board[row][col]
    #         if piece2 != "." and piece1[0] == piece2[0]:#האם זו אותה קבוצה?
    #             selected = (row, col)
    #         else:   #שלח בקשת מהלך
           
    #             move_from = selected
    #             move_to = (row, col)
    #             #בדיקה אם אפשר לעשות את הצעד הזה
    #             if if_possible(move_from,move_to,board):
    #                 if if_the_way_is_empty(move_from,move_to,board):
    #                     if if_same_color(move_from,move_to,board):
                
    #                         piece = board[move_from[0]][move_from[1]]
    #                         distance = max(
    #                             abs(move_to[0] - move_from[0]),
    #                             abs(move_to[1] - move_from[1])
    #                         )
                            
    #                         moving = {
    #                             "piece": piece,
    #                             "from": move_from,
    #                             "to": move_to,
    #                             "time_left": distance * 1000
    #                         }
    #                         # board[move_from[0]][move_from[1]] = "."
    #                         # board[move_to[0]][move_to[1]] = piece
                        
    #                         selected = None
    # elif parts[0] == "wait":
    #     ms = int(parts[1])
        
    #     if moving is not None:
    #         moving["time_left"] -= ms
        
    #         if moving["time_left"] <= 0:
    #             fr = moving["from"]
    #             to = moving["to"]
    #             #עשית צעד
    #             # if both_kings_exist(board):
    #             board[fr[0]][fr[1]] = "."
    #             board[to[0]][to[1]] = moving["piece"]
        
    #             moving = None
    #             piece = board[to[0]][to[1]]
    #             #הוספה של תרגיל 10
    #             #אם חייל הגיע לשורה האחרונה הופכים אותו למלכה
    #             if piece == "wP" and to[0] == 0:
    #                 board[to[0]][to[1]] = "wQ"
                
    #             elif piece == "bP" and to[0] == len(board) - 1:
    #                 board[to[0]][to[1]] = "bQ"
                        
                        
    # elif parts[0] == "print" and parts[1] == "board":
    #     for row in board:
    #         print(" ".join(row))   
            
            
    #לא בדקנו אם יש את שתי המלכים        
    
