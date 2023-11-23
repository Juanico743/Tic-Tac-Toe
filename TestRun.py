board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

occupied = [0]

player1 = "X"
player2 = "O"
round = 0
movingPlayer = None
status = None

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=" ")
    print("")

while round < 9:
    if round % 2 == 0:
        movingPlayer = player1
    elif round % 2 == 1:
        movingPlayer = player2

    while True:
        try:
            move = int(input(f"move (1-9): "))
            if 1 <= move <= 9:
                if move not in occupied:
                    occupied.append(move)
                    break
                else:
                    print("Try Again")
            else:
                print("Try Again")
        except (ValueError, NameError):
            print("Try Again")

    for i in range(len(board)):
        for j in range(len(board[i])):
            if move == board[i][j]:
                board[i][j] = movingPlayer
            print(board[i][j], end=" ")
        print("")

    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            status = "win"
        elif board[i][0] == board[i][1] == board[i][2]:
            status = "win"
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        status = "win"

    if status == "win":
        break
    else:
        round += 1

if status != "win":
    print(f"\nGame DRAW")
else:
    print(f"\nPlayer {movingPlayer} WINS")
