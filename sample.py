import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (118, 150, 86)
BEIGE = (238, 238, 210)

# Chess pieces (simple representation)
PIECES = {
    "bp": pygame.image.load("black_pawn.png"),
    "wp": pygame.image.load("white_pawn.png"),
}

# Resize pieces
for key in PIECES:
    PIECES[key] = pygame.transform.scale(PIECES[key], (SQUARE_SIZE, SQUARE_SIZE))

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Board setup (pawns for simplicity)
board = [
    ["bp"] * 8 if row == 1 else
    ["wp"] * 8 if row == 6 else
    [None] * 8
    for row in range(ROWS)
]

def draw_board():
    """Draws the chessboard."""
    for row in range(ROWS):
        for col in range(COLS):
            color = BEIGE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    """Draws the pieces on the board."""
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                screen.blit(PIECES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_square_under_mouse():
    """Returns the board coordinates under the mouse."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_y // SQUARE_SIZE, mouse_x // SQUARE_SIZE

def is_valid_move(piece, start, end):
    """Checks if a move is valid (basic pawn logic)."""
    start_row, start_col = start
    end_row, end_col = end

    if piece == "bp":  # Black pawn
        if start_row + 1 == end_row and start_col == end_col and not board[end_row][end_col]:
            return True
    elif piece == "wp":  # White pawn
        if start_row - 1 == end_row and start_col == end_col and not board[end_row][end_col]:
            return True
    return False

# Game loop
selected_square = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_square_under_mouse()
            if selected_square:
                start_row, start_col = selected_square
                piece = board[start_row][start_col]
                if piece and is_valid_move(piece, selected_square, (row, col)):
                    # Move piece
                    board[start_row][start_col] = None
                    board[row][col] = piece
                selected_square = None
            elif board[row][col]:
                selected_square = (row, col)

    # Draw everything
    draw_board()
    draw_pieces()

    # Highlight selected square
    if selected_square:
        pygame.draw.rect(screen, (255, 0, 0), (selected_square[1] * SQUARE_SIZE, selected_square[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

    pygame.display.flip()

pygame.quit()
sys.exit()
