import pygame, sys, random

# --- CONFIG ---
WIDTH, HEIGHT = 800, 600
CELL = 10
FPS = 20

PLAYER_COLOR = (0, 255, 255)   # Cyan
CPU_COLOR = (255, 0, 255)      # Magenta
CRASH_COLOR = (255, 180, 100)
BG_COLOR = (0, 0, 0)

# Directions (dx, dy)
DIRS = {
    "UP": (0, -1),
    "RIGHT": (1, 0),
    "DOWN": (0, 1),
    "LEFT": (-1, 0)
}
ORDERED_DIRS = ["UP", "RIGHT", "DOWN", "LEFT"]

# --- PLAYER CLASS ---
class Rider:
    def __init__(self, x, y, dir_key, color):
        self.x = x
        self.y = y
        self.dir = dir_key
        self.color = color
        self.alive = True
        self.trail = set()
        self.trail.add((x, y))

    def turn_left(self):
        i = (ORDERED_DIRS.index(self.dir) - 1) % 4
        self.dir = ORDERED_DIRS[i]

    def turn_right(self):
        i = (ORDERED_DIRS.index(self.dir) + 1) % 4
        self.dir = ORDERED_DIRS[i]

    def move(self, grid):
        if not self.alive:
            return
        dx, dy = DIRS[self.dir]
        self.x += dx
        self.y += dy

        # Collision with walls
        if not (0 <= self.x < WIDTH // CELL and 0 <= self.y < HEIGHT // CELL):
            self.alive = False
            return

        # Collision with trails
        if (self.x, self.y) in grid:
            self.alive = False
            return

        # Leave trail
        self.trail.add((self.x, self.y))
        grid.add((self.x, self.y))

    def draw(self, surf):
        for (tx, ty) in self.trail:
            pygame.draw.rect(surf, self.color, (tx * CELL, ty * CELL, CELL, CELL))
        if self.alive:
            pygame.draw.rect(surf, (255, 255, 255), (self.x * CELL, self.y * CELL, CELL, CELL), 1)

# --- GAME SETUP ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid = set()
player = Rider(10, HEIGHT // (2 * CELL), "RIGHT", PLAYER_COLOR)
cpu = Rider(WIDTH // CELL - 10, HEIGHT // (2 * CELL), "LEFT", CPU_COLOR)

running = True

# --- BASIC CPU AI ---
def cpu_decide(cpu, player, grid):
    # Try to go straight, but turn if about to crash
    dx, dy = DIRS[cpu.dir]
    nx, ny = cpu.x + dx, cpu.y + dy
    if (nx, ny) in grid or not (0 <= nx < WIDTH // CELL and 0 <= ny < HEIGHT // CELL):
        if random.random() < 0.5:
            cpu.turn_left()
        else:
            cpu.turn_right()

# --- MAIN LOOP ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.turn_left()
            elif event.key == pygame.K_RIGHT:
                player.turn_right()
            elif event.key == pygame.K_r:  # Restart
                grid = set()
                player = Rider(10, HEIGHT // (2 * CELL), "RIGHT", PLAYER_COLOR)
                cpu = Rider(WIDTH // CELL - 10, HEIGHT // (2 * CELL), "LEFT", CPU_COLOR)

    if player.alive and cpu.alive:
        cpu_decide(cpu, player, grid)
        player.move(grid)
        cpu.move(grid)

    # Draw
    screen.fill(BG_COLOR)
    player.draw(screen)
    cpu.draw(screen)

    if not player.alive or not cpu.alive:
        font = pygame.font.SysFont("monospace", 40)
        if not player.alive and not cpu.alive:
            msg = "DRAW!"
        elif player.alive:
            msg = "PLAYER WINS!"
        else:
            msg = "CPU WINS!"
        text = font.render(msg, True, (0, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 30))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
