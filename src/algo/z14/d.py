from datetime import datetime

from src.algo.z14.c import gen_new_positions


def how_many_moves(start: tuple, finish: tuple, max_dim: tuple):
    # reached = set([start])
    ROWS = max_dim[0]
    COLS = max_dim[1]
    reached = bytearray(ROWS * COLS)
    current_positions = set([start])

    moves = 0

    finish_p = finish[0] * COLS + finish[1]
    # while finish not in reached:
    while reached[finish_p] == 0:
        new_positions = set()

        # przejść przez wszystkie pozycje z current_positions
        for pos in current_positions:
            # dla kazdej wygenerowac nowe poprawne pozycje i wrzucić do n_positions
            for p in gen_new_positions(pos, max_dim):
                p_ = p[0] * COLS + p[1]
                # if p not in reached:
                if reached[p_] == 0:
                    new_positions.add(p)
                    # reached.add(p)
                    reached[p_] = 1

        moves += 1
        current_positions = new_positions
        if moves > 2 * max(max_dim):
            return None
        # print(f'move={moves}')

    return moves


if __name__ == '__main__':
    SIZE = 10000
    st = datetime.now().timestamp()
    mvs = how_many_moves((0, 0), (SIZE - 1, SIZE - 1), (SIZE, SIZE))
    en = datetime.now().timestamp()
    print(f'SIZE={SIZE}, moves={mvs}, duration={en - st:.3f}s')
