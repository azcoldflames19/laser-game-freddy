import pygame
from laser_game.level import Level

class Laser:
    def __init__(self, level):
        self.level = level
        self.path = []
        self.active = False

    def update(self):
        """Calculate the laser path based on current level state"""
        if not self.active:
            return
            
        # TODO: Implement laser path calculation with reflections
        self.path = [self.level.start_pos]  # Placeholder

    def draw(self, screen):
        """Draw the laser path"""
        if not self.path:
            return
            
        # Draw line segments
        for i in range(len(self.path)-1):
            start = self._grid_to_pixel(self.path[i])
            end = self._grid_to_pixel(self.path[i+1])
            pygame.draw.line(screen, (255, 255, 0), start, end, 3)

    def _grid_to_pixel(self, grid_pos):
        """Convert grid coordinates to screen coordinates"""
        x, y = grid_pos
        cell_size = self.level.cell_size
        margin = self.level.margin
        return (
            margin + x * cell_size + cell_size // 2,
            margin + y * cell_size + cell_size // 2
        )

    def toggle(self):
        """Toggle laser on/off"""
        self.active = not self.active
