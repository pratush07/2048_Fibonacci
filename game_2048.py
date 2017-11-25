from random import randint
def fill_rand_pos(game,rand_1=1):
    free_x_range = []
    free_y_range = []
    for i in range (len(game)):
        for j in range(len(game[0])):
            if game[i][j] == 0:
               free_x_range.append(i)
               free_y_range.append(j)
    if not free_x_range:
        return None

    for i in range(rand_1):
        if not free_x_range:
            break
        rand_pos = randint(0, len(free_x_range)-1)
        game[free_x_range[rand_pos]][free_y_range[rand_pos]] = 1
        del free_x_range[rand_pos]
        del free_y_range[rand_pos]
    return game


def generate_board(m,n):
    board = [[0 for x in range(n)] for y in range(m)]
    for i  in range (m):
        for j in range(n):
            board[i][j] = 0
    return board

def generate_fib_cache(m,n):
    term = m*n
    fib = []
    fib.append(1)
    fib.append(1)
    # reverse map
    fib_term_num_map = {}
    for i in range(2,term):
        fib.append(fib[i-1] + fib[i-2])
        fib_term_num_map[fib[i]] = i
    return {"fib_series":fib,"fib_map":fib_term_num_map}

def print_board(board):
    for i in range(len(board)):
        col = ""
        for j in range(len(board[0])):
            col += str(board[i][j])+ " "
        print col

def get_sum_list(arr,fib_dict):
    adjelem1 = -1
    sum_list = []
    for elem in arr:
        if elem:
            if adjelem1 == -1:
                adjelem1 = elem
            else:
                if (adjelem1 + elem) in fib_dict["fib_map"]:
                    sum_list.append(adjelem1 + elem)
                    adjelem1 = -1
                else:
                    sum_list.append(adjelem1)
                    adjelem1 = elem

    if adjelem1 != -1:
        sum_list.append(adjelem1)
    return sum_list


def update_board(board,strp,upd_list,dir):
    k = 0
    rows = len(board)
    cols = len(board[0])
    upd_len = len(upd_list)
    if dir == "down":
        rowctr = rows-1
        while rowctr>=0:
            if k < upd_len:
                board[rowctr][strp] = upd_list[k]
                k += 1
            else:
                board[rowctr][strp] = 0
            rowctr -=1
    elif dir == "up":
        rowctr = 0
        while rowctr<rows:
            if k < upd_len:
                board[rowctr][strp] = upd_list[k]
                k += 1
            else:
                board[rowctr][strp] = 0
            rowctr+=1
    elif dir == "right":
        colctr = cols-1
        while colctr>=0:
            if k < len(upd_list):
                board[strp][colctr] = upd_list[k]
                k += 1
            else:
                board[strp][colctr] = 0
            colctr -=1
    if dir == "left":
        colctr = 0
        while colctr<cols:
            if k < len(upd_list):
                board[strp][colctr] = upd_list[k]
                k += 1
            else:
                board[strp][colctr] = 0
            colctr += 1


def mov_dir(dir,board,fib_dict):
    cols = len(board[0])
    rows = len(board)
    if dir == "up" or dir == "down":
        for j in range(cols):
            col_arr = []
            for i in range(rows):
                col_arr.append(board[i][j])
            if dir == "down":
                col_arr.reverse()
            upd_list = get_sum_list(col_arr,fib_dict)
            update_board(board,j,upd_list,dir)

    elif dir == "left" or dir == "right":
        for i in range(rows):
            col_arr = []
            for j in range(cols):
                col_arr.append(board[i][j])
            if dir == "right":
                col_arr.reverse()
            # print col_arr
            upd_list = get_sum_list(col_arr,fib_dict)
            update_board(board,i,upd_list,dir)


def check_win(board,fib_dict):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == fib_dict["fib_series"][-1]:
                return 1
    return 0

m = int(raw_input("Please enter the number of rows(m)"))
n = int(raw_input("Please enter the number of cols(n)"))
board = generate_board(m,n)
fib_dict = generate_fib_cache(m,n)
fill_rand_pos(board,2)
print "Initial board state"
print_board(board)

dir_moves = ["up","down","left","right"]
if check_win(board, fib_dict):
    print "You won"
    exit()
while True:
    dir = raw_input("Please enter the direction(up/down/left/right). For exiting, enter exit.")
    dir = dir.lower()
    if dir == "exit":
        break
    elif dir in dir_moves:
        mov_dir(dir, board, fib_dict)
    else:
        print "Please enter a valid move"
        print_board(board)
        continue
    if check_win(board,fib_dict):
        print "You won"
        break

    if not fill_rand_pos(board):
        print "Game lost"
        break
    print_board(board)

print_board(board)
print "Thank you"