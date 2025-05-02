import pygame
import math
import random

class SolarSystem:
    """Solar system simulation for the homescreen background"""
    
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.center = (self.width // 2, self.height // 2)
        
        # Sun properties
        self.sun_radius = 40
        self.sun_color = (255, 215, 0)  # Gold
        
        # Create planets
        self.planets = []
        self.create_planets()
        
        # Stars in the background
        self.stars = []
        self.create_stars(200)  # Create 200 stars
    
    def create_planets(self):
        # Define some planet colors
        planet_colors = [
            (170, 170, 170),  # Mercury - gray
            (210, 180, 140),  # Venus - tan
            (0, 100, 200),    # Earth - blue
            (200, 100, 0),    # Mars - red
            (240, 220, 180),  # Jupiter - light brown
            (230, 220, 120),  # Saturn - yellow-ish
            (180, 210, 230),  # Uranus - light blue
            (100, 150, 240)   # Neptune - blue
        ]
        
        # Create planets with different orbits and sizes
        for i in range(8):  # 8 planets
            orbit_radius = 60 + (i * 30)  # Increasing orbit radius
            size = random.randint(5, 15) if i != 5 else random.randint(15, 25)  # Saturn is bigger
            speed = 0.5 - (i * 0.05)  # Decreasing speed for outer planets
            angle = random.uniform(0, 2 * math.pi)  # Random starting position
            
            # Add rings for Saturn (planet index 5)
            has_rings = (i == 5)
            ring_color = (200, 180, 100) if has_rings else None
            
            self.planets.append({
                'orbit_radius': orbit_radius,
                'size': size,
                'color': planet_colors[i],
                'speed': speed,
                'angle': angle,
                'has_rings': has_rings,
                'ring_color': ring_color
            })
    
    def create_stars(self, count):
        for _ in range(count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            brightness = random.randint(150, 255)
            self.stars.append({
                'pos': (x, y),
                'size': size,
                'color': (brightness, brightness, brightness)
            })
    
    def update(self):
        # Update planet positions
        for planet in self.planets:
            planet['angle'] += planet['speed'] * 0.01
            if planet['angle'] > 2 * math.pi:
                planet['angle'] -= 2 * math.pi
    
    def draw(self):
        # Fill background with dark color
        self.screen.fill((10, 10, 30))  # Dark blue/black
        
        # Draw stars
        for star in self.stars:
            pygame.draw.circle(self.screen, star['color'], star['pos'], star['size'])
        
        # Draw sun
        pygame.draw.circle(self.screen, self.sun_color, self.center, self.sun_radius)
        
        # Draw planets
        for planet in self.planets:
            # Calculate position based on orbit and angle
            x = self.center[0] + int(planet['orbit_radius'] * math.cos(planet['angle']))
            y = self.center[1] + int(planet['orbit_radius'] * math.sin(planet['angle']))
            
            # Draw orbit (faint circle)
            pygame.draw.circle(self.screen, (50, 50, 70), self.center, planet['orbit_radius'], 1)
            
            # Draw rings for Saturn
            if planet['has_rings']:
                ring_width = planet['size'] * 2
                ring_height = planet['size'] // 2
                ring_rect = pygame.Rect(
                    x - ring_width, 
                    y - ring_height // 2, 
                    ring_width * 2, 
                    ring_height
                )
                pygame.draw.ellipse(self.screen, planet['ring_color'], ring_rect, 1)
            
            # Draw planet
            pygame.draw.circle(self.screen, planet['color'], (x, y), planet['size'])
