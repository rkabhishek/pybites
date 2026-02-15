WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print(WHITE, end='')
            else:
                print(BLACK, end='')

        print()
