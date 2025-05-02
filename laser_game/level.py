import pygame
from laser_game.laser import Laser

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 60
        self.margin = 100
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        
        # Start and end points
        self.start_pos = (0, 1)  # Green start point
        self.end_pos = (width-1, height-1)  # Red end point
        
        # Editor mode flag
        self.editor_mode = True

    def draw(self, screen):
        # Draw grid
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(
                    self.margin + x * self.cell_size,
                    self.margin + y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(screen, (50, 50, 50), rect, 1)

                # Draw mirror if present
                if self.grid[y][x] and self.grid[y][x]['type'] == 'mirror':
                    center = (
                        self.margin + x * self.cell_size + self.cell_size // 2,
                        self.margin + y * self.cell_size + self.cell_size // 2
                    )
                    angle = self.grid[y][x]['angle']
                    # Calculate endpoints - always diagonal
                    if angle == 45:
                        start = (center[0] - 20, center[1] - 20)
                        end = (center[0] + 20, center[1] + 20)
                    else:  # 135 degrees
                        start = (center[0] + 20, center[1] - 20)
                        end = (center[0] - 20, center[1] + 20)
                    
                    pygame.draw.line(screen, (200, 200, 200), start, end, 3)

        # Draw start and end points
        self._draw_point(screen, self.start_pos, (0, 255, 0))  # Green for start
        self._draw_point(screen, self.end_pos, (255, 0, 0))    # Red for end

    def _draw_point(self, screen, pos, color):
        x, y = pos
        center = (
            self.margin + x * self.cell_size + self.cell_size // 2,
            self.margin + y * self.cell_size + self.cell_size // 2
        )
        pygame.draw.circle(screen, color, center, self.cell_size // 3)

    def add_mirror(self, x, y, angle):
        """Add a mirror at grid position (x,y) with given angle"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = {'type': 'mirror', 'angle': angle % 180}  # Keep angle between 0-179

    def rotate_mirror(self, x, y):
        """Rotate mirror between 45° and 135°"""
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.grid[y][x] and self.grid[y][x]['type'] == 'mirror':
                current_angle = self.grid[y][x]['angle']
                self.grid[y][x]['angle'] = 135 if current_angle == 45 else 45

    def remove_object(self, x, y):
        """Remove object at grid position (x,y)"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = None

    def grid_to_pixel(self, grid_pos):
        """Convert grid coordinates to screen coordinates"""
        x, y = grid_pos
        center = (
            self.margin + x * self.cell_size + self.cell_size // 2,
            self.margin + y * self.cell_size + self.cell_size // 2
        )
        return center
