import pygame
from laser_game.level import Level
from laser_game.laser import Laser

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Laser Reflection Game")
        self.clock = pygame.time.Clock()
        self.level = Level(10, 10)  # 10x10 grid
        self.level.add_mirror(9, 0, 45)  # Add diagonal mirror at top right corner
        self.laser = Laser(self.level)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.laser.toggle()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                if self.level.editor_mode:
                    mouse_pos = pygame.mouse.get_pos()
                    cell_size = self.level.cell_size
                    margin = self.level.margin
                    x = (mouse_pos[0] - margin) // cell_size
                    y = (mouse_pos[1] - margin) // cell_size
                    if 0 <= x < self.level.width and 0 <= y < self.level.height:
                        if self.level.grid[y][x] and self.level.grid[y][x]['type'] == 'mirror':
                            self.level.rotate_mirror(x, y)

    def update(self):
        self.laser.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen)
        self.laser.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
