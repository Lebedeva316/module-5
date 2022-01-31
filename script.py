def field1():
    print()
    print("     0  1  2  ")
    for i, row in enumerate(field):
        row_str = f"  {i}  {'  '.join(row)}  "
        print(row_str)
    print()


def ask():
    while True:
        part = input("ваш ход: ").split()

        if len(part) != 2:
            print("Необходимо две координаты")
            continue
        x, y = part
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Вне диапазона ")
            continue
        if field[x][y] != " ":
            print(" Клетка занята ")
            continue

        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("X - Победитель")
            return True
        if symbols == ["0", "0", "0"]:
            print("0 - Победитель")
            return True
    return False


field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    field1()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print("Ничья")
        break