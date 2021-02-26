import pygame


class Earth(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Earth, self).__init__()
        self.image = pygame.image.load("ground.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.field_x = x - 950
        self.field_y = y - 530

    def render(self, player_sprite):
        if abs(self.field_x - player_sprite.field_x) <= 1920 and \
                abs(self.field_y - player_sprite.field_y) <= 1080:
            self.rect.x = self.field_x - player_sprite.field_x + 950
            self.rect.y = self.field_y - player_sprite.field_y + 530