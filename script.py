board = [[" "] * 3 for i in range(3)]

def print_board():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {board[i][0]} {board[i][1]} {board[i][2]}")


def turn():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты.")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа.")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Введены неверные координаты.")
            continue

        if board[x][y] != " ":
            print("Эта клетка занята.")
            continue

        return x, y



def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X.")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0.")
            return True
    return False


count = 0
while True:
    count += 1
    print_board()
    if count % 2 == 1:
        print("Ходит крестик.")
    else:
        print("Ходит нолик.")

    x, y = turn()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья.")
        break

