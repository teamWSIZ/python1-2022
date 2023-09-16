class FastSet:

    def __init__(self, sz: int):
        self.__data = bytearray(sz)

    def __getitem__(self, item):
        elem = item // 8
        bit_idx = item % 8
        return (self.__data[elem] >> bit_idx) & 1

    def __setitem__(self, key, value):
        if not (0 <= value <= 1):
            raise ValueError('supported values: 0, 1')
        elem = key // 8
        bit_idx = key % 8
        if value == 0:
            self.__data[elem] &= ~(1 << bit_idx)
        if value == 1:
            self.__data[elem] |= (1 << bit_idx)

    def __repr__(self):
        return str(self.__data)

if __name__ == '__main__':
    c = FastSet(10)
    c[4] = 1
    print(c[4])
    c[4] = 0
    print(c[4])