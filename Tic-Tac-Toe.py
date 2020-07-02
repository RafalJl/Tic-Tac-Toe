M = [[" " for c in range(3)] for i in range(3)]

# "X", "O" in a row:
tx = ['X', 'X', 'X']
to = ['O', 'O', 'O']


def state():
    print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(M[0][0], M[0][1], M[0][2], M[1][0], M[1][1], M[1][2], M[2][0], M[2][1], M[2][2]))


def field():
    global M
    while True:
        print("Enter the coordinates:")
        cor = input().split()
        if len(cor) == 2 and cor[0] in [str(g) for g in range(0, 10)] and cor[1] in [str(g) for g in range(0, 10)]:
            cor = [int(r) for r in cor]
            y = cor[1]
            x = cor[0]
            if y in range(1, 4) and x in range(1, 4):
                if y == 3:
                    y -= 3
                elif y == 2:
                    y -= 1
                elif y == 1:
                    y += 1

                if x == 1 or x == 2 or x == 3:
                    x -= 1

                if M[y][x] != "X" and M[y][x] != "O":

                    M[y][x] = x_or_o
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    field()
                    break
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


while True:
    state()

    # how many "X", "O", " ":
    co_x = len([c for c in "".join([sth for group in M for sth in group]) if c == "X"])
    co_o = len([c for c in "".join([sth for group in M for sth in group]) if c == "O"])
    co_n = len([c for c in "".join([sth for group in M for sth in group]) if c == " "])

    if co_x <= co_o:
        x_or_o = "X"
    else:
        x_or_o = "O"

    # columns:
    c1 = [M[i][0] for i in range(3)]
    c2 = [M[i][1] for i in range(3)]
    c3 = [M[i][2] for i in range(3)]

    # diagonals:
    d1 = [M[i][i] for i in range(3)]
    d2 = [M[0][2], M[1][1], M[2][0]]

    if any([M[0] == tx, M[1] == tx, M[2] == tx, c1 == tx, c2 == tx, c3 == tx, d1 == tx, d2 == tx]):
        print("X wins")
        break
    if any([M[0] == to, M[1] == to, M[2] == to, c1 == to, c2 == to, c3 == to, d1 == to, d2 == to]):
        print("O wins")
        break
    if co_n == 0:
        print("Draw")
        break
    field()
