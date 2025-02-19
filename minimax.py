import random

BOARD_SIZE = 8

class MinimaxBot:
    def __init__(self, symbol="O"):
        self.symbol = symbol

    def get_move(self, board):
        empty_cells = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == " "]
        return random.choice(empty_cells) if empty_cells else None
