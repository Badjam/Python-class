def drawField(field):
    for row in range(5): # 0, 1,2, 3, 4
                        # 0    1      2
        if row % 2 ==0: # 0,2,4
            practicalRow = int(row/2) # 0,1,2
            for column in range(5):  # 0, 1, 2, 3, 4
                                     # 0     1     2
                if column % 2 == 0: # 0,2,4
                    practicalColumn = int(column/2) # 0,1,2
                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print(" | ", end="")
        else:
            print("----------")

player = 1
currentFiend = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(currentFiend)
while(True): # True == True
    print("Player turn: ", player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter the column\n"))
    if player == 1:
        # Make move for player 1
        if currentFiend[MoveColumn][MoveRow] == " ":
            currentFiend[MoveColumn][MoveRow] = "X"
            player = 2
    else:
        # Make move for player 2
        if currentFiend[MoveColumn][MoveRow] == " ":
            currentFiend[MoveColumn][MoveRow] = "O"
            player = 1
    drawField(currentFiend)

# def drawField(field):
#     for row in range(5):
#         if row % 2 ==0:
#             practicalRow = row/2
#             for column in range(5):
#                 if column % 2 == 0:
#                     practicalCoumn = column/2
#                     if column != 4:
#                         print(field[practicalCoumn][row], end="")
#                     else:
#                         print(field[practicalCoumn][practicalRow])
#                 else:
#                     print(" | ", end="")
#         else:
#             print("----------")
#
# player = 1
# currentField = [[" "," "," "], [" ", " ", " "], [" ", " ", " "]]
# drawField(currentField)
# while(True):
#     print(" Players turn: ", player)
#     MoveRow = int(input("Please enter the row\n"))
#     MoveColumn = int(input("Please enter the column\n"))
#     if player ==1:
#         currentField[MoveColumn][MoveRow] = "X"
#         player = 2
#
#     else:
#         currentField[MoveColumn][MoveRow] = "O"
#         player = 1
# drawField(currentField)
