# Donut Game 

import pygame, sys
from settings import Settings

class DonutGame:
  """Overall class to manage game assets and behavior."""

  def __init__(self):
    """Initialize the game, and create game resources"""
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Donut Game")

    # Set background color.
    self.bg_color = (230, 230, 230)

  def run_game(self):
    """Start the main loop for the game"""
    while True:
      # Watch for keyboard and mouse events.
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      # Redraw background during each pass through the game loop.
      self.screen.fill(self.settings.bg_color)

      # Make most recently drawn screen visible.
      pygame.display.flip()

if __name__ == '__main__':
  # Make a game instance, and run the game.
  ai = DonutGame()
  ai.run_game()