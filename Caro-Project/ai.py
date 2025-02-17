def minimax(board, depth, is_maximizing, alpha, beta):
    winner = board.check_winner()
    if winner == "X":
        return 10 - depth
    elif winner == "O":
        return depth - 10
    elif board.is_full():
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for row in range(board.size):
            for col in range(board.size):
                if board.is_valid_move(row, col):
                    board.make_move(row, col, "X")
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board.grid[row][col] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(board.size):
            for col in range(board.size):
                if board.is_valid_move(row, col):
                    board.make_move(row, col, "O")
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board.grid[row][col] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for row in range(board.size):
        for col in range(board.size):
            if board.is_valid_move(row, col):
                board.make_move(row, col, "X")
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board.grid[row][col] = ""
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move
