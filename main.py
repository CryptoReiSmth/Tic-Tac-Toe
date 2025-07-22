def print_board(board):
    print("\t1\t2\t3")
    for i in range(len(board)):
        print(f"{i+1}", end="")
        for cell in board[i]:
            print(f"\t{cell}", end="")
        print()


def get_player_move():
    move = input(f"Введите ход в виде 2 чисел через пробел: ").split()
    if len(move) != 2:
        move = input(f"Введите 2 числа через пробел: ").split()
    row, col = int(move[0]) - 1, int(move[1]) - 1
    if not (0 <= row < 3 and 0 <= col < 3):
        print(f"Координаты должны быть от 1 до 3.")
    return row, col


def check_win(board, player):
    # Горизонталь
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Вертикаль
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Главная диагональ
    if all(board[i][i] == player for i in range(3)):
        return True

    # Побочная диагональ
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Основная игра
player = "X"
board = [[" " for i in range(3)] for j in range(3)]
print("Начало игры")
print_board(board)
while not (check_win(board, "X") or check_win(board, "0")):
    row, col = get_player_move()
    board[row][col] = player

    if player == "X":
        player = "0"
    else:
        player = "X"
    print_board(board)
if player == "X":
    player = "0"
else:
    player = "X"
    print(f"Выиграл игрок {player}")


