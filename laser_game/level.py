import pygame

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 60
        self.margin = 100
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        
        # Placeholder for start and end points
        self.start_pos = (0, 0)
        self.end_pos = (width-1, height-1)
        
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
            self.grid[y][x] = {'type': 'mirror', 'angle': angle}

    def remove_object(self, x, y):
        """Remove object at grid position (x,y)"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = None
