board = [None, None, None, None, None, None, None, None, None]
def print_board():
        for i in range(3):
            for j in range(3):
                if board[i * 3 + j] is None:
                    print('_', end=' ')
                else:
                    print(board[i * 3 + j], end=' ')
            print("")
def check_win():
    global who_won
    who_won = None
    if board[0]==board[1]==board[2]!=None:
        who_won = board[0]
        return True
    elif board[3]==board[4]==board[5]!=None:
        who_won = board[3]
        return True
    elif board[6]==board[7]==board[8]!=None:
        who_won = board[6]
        return True
    elif board[0]==board[3]==board[6]!=None:
        who_won = board[0]
        return True
    elif board[1]==board[4]==board[7]!=None:
        who_won = board[1]
        return True
    elif board[2]==board[5]==board[8]!=None:
        who_won = board[2]
        return True
    elif board[0]==board[4]==board[8]!=None:
        who_won = board[0]
        return True
    elif board[2]==board[4]==board[6]!=None:
        who_won = board[2]
        return True
    else:
        return False
def utility():
    if check_win() and who_won == "X":
        return -1
    elif check_win() and who_won == "O":
        return 1
    elif not check_win() and not (None in board):
        return 0
def mini():
    if check_win() or not (None in board):
        return utility()

    value = float("inf")
    for i in range(len(board)):
        if board[i] == None:
            board[i] = "X"
            value = min(value, maxi())
            board[i] = None
    return value
def maxi():
    if check_win() or not (None in board):
        return utility()

    value = -float("inf")
    for i in range(len(board)):
        if board[i] == None:
            board[i] = "O"
            value = max(value, mini())
            board[i] = None
    return value
def dr_strange():
    best_value = -float("inf")
    best_move = None

    for i in range(len(board)):
        if board[i] == None:
            board[i] = "O"
            move_value = mini()
            board[i] = None

            if move_value > best_value:
                best_value = move_value
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
while True:
    location = int(input("Where you wanna play? (0-8): "))
    if board[location] is not None:
        print("You can't play there, stupid bitch!")
        continue
    board[location] = "X"
    print_board()

    if check_win():
        print(f"{who_won} won!")
        break
    elif not (None in board):
        print("Draw!")
        break

    dr_strange()
    print("----------------------")
    print_board()

    if check_win():
        print(f"{who_won} won!")
        break
    elif not (None in board):
        print("Draw!")
        break





