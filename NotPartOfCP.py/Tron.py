import pygame, sys, random

# --- CONFIG ---
WIDTH, HEIGHT = 800, 600
CELL = 10
FPS = 20

PLAYER_COLOR = (0, 255, 255)
CPU_COLOR = (255, 0, 255)
BG_COLOR = (0, 0, 0)

# Directions
DIRS = {"UP": (0, -1), "RIGHT": (1, 0), "DOWN": (0, 1), "LEFT": (-1, 0)}
ORDERED_DIRS = ["UP", "RIGHT", "DOWN", "LEFT"]

# --- PLAYER CLASS ---
class Rider:
    def __init__(self, x, y, dir_key, color):
        self.x, self.y = x, y
        self.dir = dir_key
        self.color = color
        self.alive = True
        self.trail = {(x, y)}

    def turn_left(self): self.dir = ORDERED_DIRS[(ORDERED_DIRS.index(self.dir) - 1) % 4]
    def turn_right(self): self.dir = ORDERED_DIRS[(ORDERED_DIRS.index(self.dir) + 1) % 4]

    def move(self, grid):
        if not self.alive: return
        dx, dy = DIRS[self.dir]
        self.x += dx; self.y += dy

        if not (0 <= self.x < WIDTH // CELL and 0 <= self.y < HEIGHT // CELL):
            self.alive = False; return
        if (self.x, self.y) in grid:
            self.alive = False; return

        self.trail.add((self.x, self.y))
        grid.add((self.x, self.y))

    def draw(self, surf):
        for (tx, ty) in self.trail:
            pygame.draw.rect(surf, self.color, (tx * CELL, ty * CELL, CELL, CELL))
        if self.alive:
            pygame.draw.rect(surf, (255, 255, 255), (self.x * CELL, self.y * CELL, CELL, CELL), 1)

# --- RESET FUNCTION ---
def reset():
    global grid, player, cpu
    grid = set()
    player = Rider(10, HEIGHT // (2 * CELL), "RIGHT", PLAYER_COLOR)
    cpu = Rider(WIDTH // CELL - 10, HEIGHT // (2 * CELL), "LEFT", CPU_COLOR)

# --- CPU AI ---
def cpu_decide(cpu, player, grid):
    dx, dy = DIRS[cpu.dir]
    nx, ny = cpu.x + dx, cpu.y + dy
    if (nx, ny) in grid or not (0 <= nx < WIDTH // CELL and 0 <= ny < HEIGHT // CELL):
        if random.random() < 0.5: cpu.turn_left()
        else: cpu.turn_right()

# --- GAME SETUP ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 30)

# Restart button rectangle
button_rect = pygame.Rect(WIDTH // 2 - 80, HEIGHT // 2 + 40, 160, 50)

reset()
running = True

# --- MAIN LOOP ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: player.turn_left()
            elif event.key == pygame.K_RIGHT: player.turn_right()
            elif event.key == pygame.K_r: reset()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                reset()

    if player.alive and cpu.alive:
        cpu_decide(cpu, player, grid)
        player.move(grid); cpu.move(grid)

    # Draw background
    screen.fill(BG_COLOR)
    player.draw(screen); cpu.draw(screen)

    # End of game screen
    if not player.alive or not cpu.alive:
        if not player.alive and not cpu.alive: msg = "DRAW!"
        elif player.alive: msg = "PLAYER WINS!"
        else: msg = "CPU WINS!"

        text = font.render(msg, True, (0, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 40))

        # Draw Restart button
        pygame.draw.rect(screen, (50, 50, 50), button_rect)
        pygame.draw.rect(screen, (0, 255, 255), button_rect, 2)
        button_text = font.render("RESTART", True, (0, 255, 255))
        screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2,
                                  button_rect.centery - button_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
