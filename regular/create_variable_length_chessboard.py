WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    seq = (WHITE, BLACK)
    row_index = 0
    for row in range(size):
        col_index = row_index
        for col in range(size):
            print(seq[col_index], end='')
            col_index = 1 - col_index

        print()
        row_index = 1 - row_index
