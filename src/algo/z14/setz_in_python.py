from utils import ts




st = ts()

M, N = 10 ** 4, 10 ** 4

# s = set()
bs = bytearray(M * N)

for row in range(M):
    for col in range(N):
        # s.add((i,j))
        bs[row * N + col] = 1

en = ts()

# 700MB = 7 * 10**8 ---> 10**7 elementów, ~70B/tuple
# 8.7GB ~= 8.7 * 10**9 --> 10**8 ;; 80B per tuple

print(f'allocating {M * N // 10 ** 6} mln elements took {en - st:.3f}s')

g = input('end it? ')
