import pygame

def draw_grid(screen, size, cell_size):
    for i in range(1, size):
        pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (size * cell_size, i * cell_size), 2)
        pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, size * cell_size), 2)

def draw_marks(screen, board, cell_size):
    font = pygame.font.Font(None, 120)
    for row in range(board.size):
        for col in range(board.size):
            mark = board.grid[row][col]
            if mark != "":
                text = font.render(mark, True, (0, 0, 0))
                screen.blit(text, (col * cell_size + 20, row * cell_size + 10))
