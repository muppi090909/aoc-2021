import os
# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "exm_input.txt")
fh = open(fpath)

# Loop to read-in the input data
draw = None
boards = []  # List of Boards
current_board = []
while True:
    line = fh.readline()
    # Line is Empty in case of EOF
    # Insert the last board, cleanup and then break
    if line == '':
        boards.append(current_board)
        fh.close()
        del fpath
        del dirpath
        break    

    # Else strip the newline before any processing
    line = line.strip()
    
    # Read the bingo numbers drawn
    if draw == None:
        line = line.replace(',', ' ')
        draw = line.split()
    else:
        # boards are separated by empty lines
        if line == '':
            # each board has 5 rows
            # initialise the board for every 5th row
            if len(current_board) == 5:
                boards.append(current_board)
            # initialise the current board
            current_board = []
        else:
            # this is not empty row
            # so read in the current line to the board
            current_row = line.split()
            current_board.append(current_row)

for entry in draw:
    for number,board in enumerate(boards):
        for row in range(0, 5):
            if entry in board[row]:
                col = board[row].index(entry)
                board[row][col] = -1

                # check for win
                win = False
                if board[row].count(-1) == 5:
                    win = True
                else:
                    for i in range(0, 5):
                        if board[i][col] != -1:
                            break
                    if i == 5:
                        win = True
                if win == True:
                    #sum of unmarked
                    sou = 0
                    for win_board in board:
                        for j in range(0, 5):
                            if win_board[j] != -1:
                                sou += int(win_board[j])
                    boards[number].append(True)
                winners = 0
                for m in boards:
                    if True == m[len(m)-1]:
                        winners += 1
                if winners == len(boards)-1:
                    sou = 0
                    for win_board in board:
                        if win_board == True:
                            break
                        for n in range(0, 5):
                            if win_board[n] != -1:
                                sou += int(win_board[n])
                    print(int(entry)*sou)