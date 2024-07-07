import pygame

class Koen:
  """A class to manage Koen's actions."""

  def __init__(self, Donut_game):
    """Initialize Koen and set his starting position."""
    self.screen = Donut_game.screen
    self.settings = Donut_game.settings
    self.screen_rect = Donut_game.screen.get_rect()

    # Load Koen's image and get its rect.
    self.image = pygame.image.load('images/K1_S.png').convert_alpha()
    self.rect = self.image.get_rect()

    # Set the start position at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom

    # Store a decimal value for Koen's horizontal position.
    self.x = float(self.rect.x)

    # Movement flags.
    self.move_right = False
    self.move_left = False

  def update(self):
    """Update Koen's position based on movement status flag."""
    # Update Koen's x value, not the rect value.

    if self.move_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.koen_speed
    if self.move_left and self.rect.left > 0:
      self.x -= self.settings.koen_speed

    # Update rect object from self.x
    self.rect.x = self.x

  def blitme(self):
    """Draw Koen at his current location"""
    self.screen.blit(self.image, self.rect)