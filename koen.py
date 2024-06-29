import pygame

class Koen:
  """A class to manage Koen's actions."""

  def __init__(self, Donut_game):
    """Initialize Koen and set his starting position."""
    self.screen = Donut_game.screen
    self.screen_rect = Donut_game.screen.get_rect()

    # Load Koen's image and get its rect.
    self.image = pygame.image.load('images/K1_S.png').convert_alpha()
    self.rect = self.image.get_rect()

    # Set the start position at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom

  def blitme(self):
    """Draw Koen at his current location"""
    self.screen.blit(self.image, self.rect)