# -*- coding: utf-8 -*-

class Board:
    BLANK = 0                           # 何も置かれていない
    WHITE = 1                           # 白い駒が置かれている
    BLACK = 2                           # 黒い駒が置かれている

    def __init__(self):
        # 盤面を初期化する
        self.board = [[0] * 8 for x in range(8)]

    def set_white(self, x, y):
        # クラスのアトリビュートを代入して、盤面に白い駒を置く
        self.board[x][y] = self.WHITE
