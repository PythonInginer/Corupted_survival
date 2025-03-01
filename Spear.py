import pygame


class Spear(pygame.sprite.Sprite):
    def __init__(self):
        super(Spear, self).__init__()
        self.image = pygame.image.load("data/tools/spear.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.field_x = -1
        self.field_y = -1
        self.name = "spear"

    def render(self, player_sprite):
        if abs(self.field_x - player_sprite.field_x) <= 1920 and \
                abs(self.field_y - player_sprite.field_y) <= 1080:
            self.rect.x = self.field_x - player_sprite.field_x + 950
            self.rect.y = self.field_y - player_sprite.field_y + 530