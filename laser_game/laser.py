import pygame

class Laser:
    def __init__(self, level):
        self.level = level
        self.path = []
        self.active = False

    def update(self):
        """Calculate the laser path based on current level state"""
        if not self.active:
            return
            
        self.path = []
        current_pos = self.level.start_pos
        direction = (1, 0)  # Start moving right
        visited = set()

        while True:
            if current_pos in visited:
                break  # Prevent infinite loop
            visited.add(current_pos)
            self.path.append(current_pos)

            # Check if we reached the end
            if current_pos == self.level.end_pos:
                break

            # Get next position
            next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

            # Check boundary
            if not (0 <= next_pos[0] < self.level.width and 0 <= next_pos[1] < self.level.height):
                break

            # Check for mirror
            cell = self.level.grid[next_pos[1]][next_pos[0]]
            if cell and cell['type'] == 'mirror':
                direction = (-direction[1], -direction[0])  # 90 degree reflection

            current_pos = next_pos

    def draw(self, screen):
        """Draw the laser path"""
        if not self.path:
            return
            
        # Draw line segments
        for i in range(len(self.path)-1):
            start = self.level.grid_to_pixel(self.path[i])
            end = self.level.grid_to_pixel(self.path[i+1])
            pygame.draw.line(screen, (255, 255, 0), start, end, 3)

    def toggle(self):
        """Toggle laser on/off"""
        self.active = not self.active
