import pygame
from laser_game.level import Level
from laser_game.laser import Laser
from laser_game.screens import HomeScreen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Laser Reflection Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # Game state
        self.in_game = False

        # Initialize level and laser (will be set up when starting the game)
        self.level = None
        self.laser = None

        # Win condition state
        self.showing_win_popup = False
        self.font = pygame.font.SysFont('Arial', 36)
        self.win_message = self.font.render('Laser has reached the end!', True, (255, 255, 0))

    def setup_game(self):
        """Initialize the game level and laser"""
        self.level = Level(10, 10)  # 10x10 grid
        self.level.add_mirror(9, 1, 45)  # Add diagonal mirror at (9,1)
        self.laser = Laser(self.level)
        self.in_game = True

    def run(self):
        """Main game loop with homescreen"""
        while self.running:
            # Show homescreen
            home_screen = HomeScreen(self)
            home_screen.run()

            # If user quit from homescreen, exit
            if not self.running:
                break

            # Set up and start the game
            self.setup_game()

            # Main game loop
            while self.running and self.in_game:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(60)

            # If we exited the game loop but the game is still running,
            # we'll loop back to show the homescreen again

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Only process game-specific events if in game
            if not self.in_game:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.laser.toggle()
                    # Reset win popup when toggling laser
                    self.showing_win_popup = False
                # Close win popup with any key
                elif self.showing_win_popup:
                    self.showing_win_popup = False
                # Return to homescreen with Escape key
                elif event.key == pygame.K_ESCAPE:
                    self.in_game = False
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Close win popup with any mouse click
                if self.showing_win_popup:
                    self.showing_win_popup = False
                # Handle mirror rotation
                elif event.button == 1 and self.level.editor_mode:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    cell_size = self.level.cell_size
                    margin = self.level.margin
                    x = (mouse_pos[0] - margin) // cell_size
                    y = (mouse_pos[1] - margin) // cell_size
                    if 0 <= x < self.level.width and 0 <= y < self.level.height:
                        if self.level.grid[y][x] and self.level.grid[y][x]['type'] == 'mirror':
                            self.level.rotate_mirror(x, y)

    def update(self):
        # Only update game elements if in game
        if not self.in_game:
            return

        self.laser.update()

        # Check for win condition
        if self.laser.has_reached_end and not self.showing_win_popup:
            self.showing_win_popup = True

    def draw(self):
        # Only draw game elements if in game
        if not self.in_game:
            return

        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen)
        self.laser.draw(self.screen)

        # Draw win popup if needed
        if self.showing_win_popup:
            self.draw_win_popup()

        pygame.display.flip()

    def draw_win_popup(self):
        # Add a semi-transparent overlay to darken the background
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))  # Semi-transparent black
        self.screen.blit(overlay, (0, 0))

        # Draw popup box
        popup_width, popup_height = 500, 200
        popup_x = (self.screen.get_width() - popup_width) // 2
        popup_y = (self.screen.get_height() - popup_height) // 2
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)

        # Draw shadow (multiple rectangles with decreasing alpha)
        shadow_offset = 10
        shadow_alpha_start = 100
        shadow_steps = 5

        for i in range(shadow_steps):
            alpha = shadow_alpha_start - (i * (shadow_alpha_start // shadow_steps))
            offset = i * (shadow_offset // shadow_steps)
            shadow_surface = pygame.Surface((popup_width, popup_height), pygame.SRCALPHA)
            shadow_surface.fill((0, 0, 0, alpha))
            self.screen.blit(shadow_surface, (popup_x + offset, popup_y + offset))

        # Draw popup background
        pygame.draw.rect(self.screen, (60, 60, 70), popup_rect)  # Slightly blue-gray background

        # Add subtle inner highlight
        highlight_rect = pygame.Rect(popup_x + 2, popup_y + 2, popup_width - 4, popup_height - 4)
        pygame.draw.rect(self.screen, (70, 70, 80), highlight_rect)

        # Draw message
        text_rect = self.win_message.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(self.win_message, text_rect)

        # Draw instruction
        instruction_font = pygame.font.SysFont('Arial', 24)
        instruction = instruction_font.render('Press any key to continue', True, (200, 200, 200))
        instruction_rect = instruction.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))
        self.screen.blit(instruction, instruction_rect)

if __name__ == "__main__":
    game = Game()
    game.run()
