import numpy as np

MINOS = [[[0, 0, 0, 0],
          [2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],

         [[3, 0, 0],
          [3, 3, 3],
          [0, 0, 0]],

         [[0, 0, 4],
          [4, 4, 4],
          [0, 0, 0]],

         [[0, 5, 5],
          [5, 5, 0],
          [0, 0, 0]],

         [[6, 6, 0],
          [0, 6, 6],
          [0, 0, 0]],

         [[0, 7, 0],
          [7, 7, 7],
          [0, 0, 0]],

         [[8, 8],
          [8, 8]]]


class Mino():
    def __init__(self, x, y, type_):
        self.x = x
        self.y = y
        self.type_ = type_
        self.mino = np.array(MINOS[type_])

    def collision(self, board):
        h, w = self.mino.shape
        return np.sum(board[self.y:self.y+h, self.x:self.x+w]*self.mino) > 0

    def copy(self):
        new_mino = Mino(self.x, self.y, self.type_)
        new_mino.mino = np.copy(self.mino)
        return new_mino
