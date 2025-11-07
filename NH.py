import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8

# Colors
WHITE = (255, 255, 255)
BLACK = (118, 150, 86)
LIGHT_BROWN = (238, 238, 210)
DARK_BROWN = (118, 150, 86)

# Load chess pieces
pieces = {}
for piece in ['wp', 'wr', 'wn', 'wb', 'wq', 'wk', 
               'bp', 'br', 'bn', 'bb', 'bq', 'bk']:
    pieces[piece] = pygame.transform.scale(
        pygame.image.load(f"https://raw.githubusercontent.com/lichess-org/lila/master/public/piece/cburnett/{piece}.png"),
        (SQUARE_SIZE, SQUARE_SIZE)
    )

# Board setup
board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["wp"] * 8,
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess")

# Variables
selected = None
running = True

def draw_board():
    """Draw the chessboard and pieces."""
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            piece = board[row][col]
            if piece != "":
                screen.blit(pieces[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_square(pos):
    """Convert mouse position to board coordinates."""
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

# Game loop
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_square(pygame.mouse.get_pos())
            if selected:
                prev_row, prev_col = selected
                board[row][col], board[prev_row][prev_col] = board[prev_row][prev_col], ""
                selected = None
            else:
                if board[row][col] != "":
                    selected = (row, col)

pygame.quit()
# --- End of the Chess Game Code ---
