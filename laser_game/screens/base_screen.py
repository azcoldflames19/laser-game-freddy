import pygame

class BaseScreen:
    """Base class for all screens in the game"""
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.running = True
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.running = False
    
    def update(self):
        """Update screen state"""
        pass
    
    def draw(self):
        """Draw screen elements"""
        pass
    
    def run(self):
        """Main loop for the screen"""
        self.running = True
        while self.running and self.game.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.game.clock.tick(60)
