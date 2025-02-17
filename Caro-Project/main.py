import pygame
from board import Board
from ai import find_best_move
from utils import draw_grid, draw_marks

CELL_SIZE = 100
PLAYER_O = "O"
PLAYER_X = "X"


def main():
    pygame.init()

    size = 3  # Change to 4 for a 4x4 board
    board = Board(size)
    screen = pygame.display.set_mode((size * CELL_SIZE, size * CELL_SIZE))
    pygame.display.set_caption("Tic Tac Toe")

    running = True
    current_player = PLAYER_O

    while running:
        screen.fill((255, 255, 255))
        draw_grid(screen, size, CELL_SIZE)
        draw_marks(screen, board, CELL_SIZE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and current_player == PLAYER_O:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if board.make_move(row, col, PLAYER_O):
                    if board.check_winner() or board.is_full():
                        running = False
                    current_player = PLAYER_X

        if current_player == PLAYER_X:
            best_move = find_best_move(board)
            if best_move:
                board.make_move(best_move[0], best_move[1], PLAYER_X)
            if board.check_winner() or board.is_full():
                running = False
            current_player = PLAYER_O

    pygame.quit()


if __name__ == "__main__":
    main()
