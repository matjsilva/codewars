# goodSudoku1 = Sudoku([
#   [7,8,4, 1,5,9, 3,2,6],
#   [5,3,9, 6,7,2, 8,4,1],
#   [6,1,2, 4,3,8, 7,5,9],

#   [9,2,8, 7,1,5, 4,6,3],
#   [3,5,7, 8,4,6, 1,9,2],
#   [4,6,1, 9,2,3, 5,8,7],
  
#   [8,7,6, 3,9,4, 2,1,5],
#   [2,4,3, 5,6,1, 9,7,8],
#   [1,9,5, 2,8,7, 6,3,4]
# ])

# badSudoku1 = Sudoku([
#   [0,2,3, 4,5,6, 7,8,9],
#   [1,2,3, 4,5,6, 7,8,9],
#   [1,2,3, 4,5,6, 7,8,9],
  
#   [1,2,3, 4,5,6, 7,8,9],
#   [1,2,3, 4,5,6, 7,8,9],
#   [1,2,3, 4,5,6, 7,8,9],
  
#   [1,2,3, 4,5,6, 7,8,9],
#   [1,2,3, 4,5,6, 7,8,9],
#   [1,2,3, 4,5,6, 7,8,9]
# ])

# regras para validação
# ---------------------
# Data structure dimension: NxN where N > 0 and √N == integer
# Rows may only contain integers: 1..N (N included)
# Columns may only contain integers: 1..N (N included)
# 'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

from math import sqrt

class Sudoku(object):
    def __init__(self, data): # preparando vars
        self.data = data 
        self.n = 0
        self.blockLen = 0

    def is_valid(self): # função principal
        self.n = len(self.data)
        try:
            self.blockLen = int(sqrt(self.n))
        except ValueError:
            return False
        if any([len(row) != self.n for row in self.data]):
            return False
        return all([self._is_valid_row(i)
                    and self._is_valid_column(i)
                    and self._is_valid_block(i)
                    for i in range(self.n)])

    def _is_valid_row(self, row_num): # teste das linhas
        return self._is_valid_set(set(self.data[row_num]))

    def _is_valid_column(self, column_num): # teste das colunas
        return self._is_valid_set(set([self.data[r][column_num] for r in range(self.n)]))

    def _is_valid_block(self, block_num): # teste de NxN (linhas, colunas)
        block_row_num, block_column_num = divmod(block_num, self.blockLen)
        block_row, block_column = block_row_num * self.blockLen, block_column_num * self.blockLen
        block_set = set()
        for r in range(block_row, block_row + self.blockLen):
            for c in range(block_column, block_column + self.blockLen):
                block_set.add(self.data[r][c])
        return self._is_valid_set(block_set)

    def _is_valid_set(self, num_set): # resultado
        return len(num_set) == self.n \
               and max(num_set) == self.n \
               and min(num_set) == 1 \
               and all(type(i) is int for i in num_set)
