import random

import pygame


class Flint(pygame.sprite.Sprite):
    def __init__(self):
        super(Flint, self).__init__()
        self.image = pygame.image.load("data/materials/flint.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.field_x = random.randint(-950, 950)
        self.field_y = random.randint(-530, 530)
        self.name = "flint"

    def render(self, player_sprite):
        if abs(self.field_x - player_sprite.field_x) <= 1920 and \
                abs(self.field_y - player_sprite.field_y) <= 1080:
            self.rect.x = self.field_x - player_sprite.field_x + 950
            self.rect.y = self.field_y - player_sprite.field_y + 530