import pygame
from laser_game.screens.base_screen import BaseScreen
from laser_game.screens.solar_system import SolarSystem

class Button:
    """A simple button class for UI elements"""
    
    def __init__(self, x, y, width, height, text, font, text_color=(255, 255, 255), 
                 bg_color=(60, 60, 70), hover_color=(80, 80, 100)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.is_hovered = False
        
        # Pre-render text
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
    
    def update(self, mouse_pos):
        """Update button state based on mouse position"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):
        """Draw the button on the screen"""
        # Draw button background
        color = self.hover_color if self.is_hovered else self.bg_color
        pygame.draw.rect(screen, color, self.rect)
        
        # Draw button shadow
        shadow_offset = 5
        shadow_rect = pygame.Rect(
            self.rect.x + shadow_offset,
            self.rect.y + shadow_offset,
            self.rect.width,
            self.rect.height
        )
        shadow_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        shadow_surface.fill((0, 0, 0, 100))  # Semi-transparent black
        screen.blit(shadow_surface, (self.rect.x + shadow_offset, self.rect.y + shadow_offset))
        
        # Draw button on top of shadow
        pygame.draw.rect(screen, color, self.rect)
        
        # Add a border
        pygame.draw.rect(screen, (100, 100, 120), self.rect, 2)
        
        # Draw text
        screen.blit(self.text_surface, self.text_rect)
    
    def is_clicked(self, event):
        """Check if button was clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False


class HomeScreen(BaseScreen):
    """Home screen with solar system background and play button"""
    
    def __init__(self, game):
        super().__init__(game)
        
        # Create solar system background
        self.solar_system = SolarSystem(self.screen)
        
        # Create title text
        self.title_font = pygame.font.SysFont('Arial', 64, bold=True)
        self.title_text = self.title_font.render('Laser Reflection Game', True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.screen.get_width() // 2, 150))
        
        # Create button font
        self.button_font = pygame.font.SysFont('Arial', 36)
        
        # Create play button
        button_width, button_height = 200, 60
        button_x = (self.screen.get_width() - button_width) // 2
        button_y = self.screen.get_height() - 200
        self.play_button = Button(
            button_x, button_y, button_width, button_height,
            'Play', self.button_font
        )
    
    def handle_events(self):
        """Handle pygame events"""
        mouse_pos = pygame.mouse.get_pos()
        self.play_button.update(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.running = False
            
            # Check for button click
            if self.play_button.is_clicked(event):
                self.running = False  # Exit homescreen to start the game
    
    def update(self):
        """Update screen state"""
        self.solar_system.update()
    
    def draw(self):
        """Draw screen elements"""
        # Draw solar system background
        self.solar_system.draw()
        
        # Draw title
        self.screen.blit(self.title_text, self.title_rect)
        
        # Draw play button
        self.play_button.draw(self.screen)
