class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["" for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row, col):
        return self.grid[row][col] == ""

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.grid[row][col] = player
            return True
        return False

    def check_winner(self):
        for i in range(self.size):
            if all(self.grid[i][j] == "O" for j in range(self.size)) or \
               all(self.grid[j][i] == "O" for j in range(self.size)):
                return "O"
            if all(self.grid[i][j] == "X" for j in range(self.size)) or \
               all(self.grid[j][i] == "X" for j in range(self.size)):
                return "X"

        if all(self.grid[i][i] == "O" for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == "O" for i in range(self.size)):
            return "O"
        if all(self.grid[i][i] == "X" for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == "X" for i in range(self.size)):
            return "X"

        return None

    def is_full(self):
        return all(self.grid[row][col] != "" for row in range(self.size) for col in range(self.size))
