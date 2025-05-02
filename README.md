# Laser Reflection Game

A laser reflection puzzle game with a solar system homescreen and level editor.

## Current Features

- Interactive homescreen with solar system simulation background
- Win condition detection with popup message
- 10x10 grid with adjustable cell size
- Start (green) and end (red) point
- Laser path calculation with mirror reflections
- Keyboard control to toggle laser on/off (SPACE key)
- Editor mode for mirror placement and rotation
- Smooth UI with shadow effects

## How to Play

1. Run the game with `python -m laser_game.main`
2. On the homescreen, click the "Play" button to start the game
3. In the game, press SPACE to toggle the laser on/off
4. Guide the laser from the green start point to the red end point using mirrors
5. When the laser reaches the end point, a win message will appear
6. Press any key to dismiss the win message
7. Press ESC to return to the homescreen

## Controls

- **Homescreen:**
  - Click "Play" to start the game
  - Close the window to exit

- **Game:**
  - SPACE: Toggle laser on/off
  - ESC: Return to homescreen
  - Left-click: Rotate mirrors (in editor mode)
  - Any key/click: Dismiss win popup

## Project Structure

- `laser_game/`: Main game package
  - `main.py`: Main game loop and core functionality
  - `laser.py`: Laser path calculation
  - `level.py`: Level grid and mirror management
  - `screens/`: UI screens
    - `homescreen.py`: Homescreen with solar system
    - `solar_system.py`: Solar system simulation
    - `base_screen.py`: Base class for all screens

## Future Features

- Level saving/loading
- Multiple levels with increasing difficulty
- Level selection screen
- Custom level editor
- Sound effects and music
- More mirror types and obstacles

## Requirements

- Python 3.x
- Pygame 2.x
