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
            # Editor controls will be added here

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
