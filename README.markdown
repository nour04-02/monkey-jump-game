# Monkey Jump Game

Monkey Jump is a 2D platformer game built with Pygame, where players control a monkey navigating through randomly generated platforms while avoiding enemies. The goal is to climb as high as possible to achieve a high score, with moving platforms and enemies adding challenge after reaching certain score thresholds. The game features a high score system, smooth animations, and sound effects for an engaging experience.

## Features
- **Dynamic Platforms**: Randomly generated static and moving platforms.
- **Enemy Challenges**: Enemies spawn after a score of 150, moving horizontally across the screen.
- **Score System**: Tracks current and high scores, saved to a file.
- **Controls**: Left/Right arrow keys for movement, automatic jumping on platform collision.
- **Game Over**: Triggered by falling off-screen or colliding with enemies, with a restart option via the spacebar.

## Installation
1. Ensure Python and Pygame are installed (`pip install pygame`).
2. Clone the repository and place the `pics/` folder (containing images and sound) in the project directory.
3. Run `main.py` to start the game.

## Assets
- Images: `back1.jpg` (background), `nope1.png` (player), `floor.png` (platform), `enemy.png` (enemy sprite sheet).
- Sound: `cartoon-jump-6462.mp3` (jump sound effect).

## How to Play
- Use **Left/Right Arrow Keys** to move the monkey.
- Land on platforms to jump and climb higher.
- Avoid enemies and falling off-screen.
- Press **Spacebar** to restart after a game over.

## Files
- `main.py`: Core game loop and logic.
- `MonkeyPlayer.py`: Player class for movement and collision.
- `PlatForms.py`: Platform class for static and moving platforms.
- `Enemy.py`: Enemy class and sprite sheet handling.
- `highScore.txt`: Stores the highest score.