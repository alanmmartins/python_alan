import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Definir dimensiones de la pantalla
WIDTH = HEIGHT = 640
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION

# Cargar imágenes de piezas de ajedrez
images = {}
pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
for piece in pieces:
    images[piece] = pygame.image.load(f"images/{piece}.png")

# Definir el tablero de ajedrez
board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
]

# Iniciar la ventana de Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Definir función para dibujar el tablero de ajedrez
def draw_board():
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = board[row][col]
            if piece:
                screen.blit(images[piece], pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Iniciar el loop principal de Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_board()
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
