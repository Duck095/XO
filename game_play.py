BOARD_SIZE = 8

def check_winner(board, symbol):
    for row in board:
        if "".join(row).count(symbol * 5):
            return True
    for col in range(BOARD_SIZE):
        if "".join([board[row][col] for row in range(BOARD_SIZE)]).count(symbol * 5):
            return True
    return False

def get_empty_cells(board):
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == " "]

def play_game(bot1, bot2):
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    turn = 0

    while get_empty_cells(board):
        bot = bot1 if turn % 2 == 0 else bot2
        move = bot.get_move(board)

        if move:
            r, c = move
            board[r][c] = "X" if turn % 2 == 0 else "O"
            if check_winner(board, "X"):
                return "Minimax" if bot1.symbol == "X" else "DQN"
            if check_winner(board, "O"):
                return "DQN" if bot2.symbol == "O" else "Minimax"

        turn += 1
    return "Draw"
