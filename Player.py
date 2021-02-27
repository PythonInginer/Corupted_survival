import pygame

from recipes import recipes
from Axe import Axe
from PickAxe import PickAxe


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("data/skins/player.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.move_directions = []
        self.field_x = 0
        self.field_y = 0

        self.inventory = {}
        self.active = 0
        self.active_in_menu = 0
        self.can_move = True

    def move(self, tick):
        if self.can_move:
            self.step = round(200 * tick / 1000)
            for i in self.move_directions:
                if i == "left":
                    self.field_x += -self.step
                elif i == "right":
                    self.field_x += self.step
                elif i == "up":
                    self.field_y += -self.step
                elif i == "down":
                    self.field_y += self.step

    def draw_gui(self, screen):
        k = 0
        for i in range(9):
            if i == self.active:
                pygame.draw.rect(screen, "white", (100 * i + 200, 980, 100, 100), 6)
            else:
                pygame.draw.rect(screen, "white", (100 * i + 200, 980, 100, 100), 1)
        for i in self.inventory.keys():
            temp = pygame.sprite.Group()
            self.inventory[i][0].rect.x = 100 * k + 200
            self.inventory[i][0].rect.y = 980
            font = pygame.font.Font(None, 50)
            text = font.render(str(len(self.inventory[i])), True, (100, 255, 100))
            screen.blit(text, (100 * k + 200, 1030))
            temp.add(self.inventory[i][0])
            temp.draw(screen)
            temp.empty()
            k += 1

        if not self.can_move:
            for i in range(3):
                if i == 1:
                    pygame.draw.rect(screen, "white", (10, 100 * i + 100, 100, 100), 6)
                else:
                    pygame.draw.rect(screen, "white", (10, 100 * i + 100, 100, 100), 1)

            k = 0
            group = pygame.sprite.Group()
            for i in recipes.keys():
                if i == "axe":
                    sprite = Axe()
                elif i == "pickaxe":
                    sprite = PickAxe()
                sprite.rect.x = 10
                sprite.rect.y = 100 * k + 100
                group.add(sprite)
                k += 1
            group.draw(screen)

    def change_active(self, number):
        self.active = number

    def change_active_with_mouse(self, number):
        if 0 <= self.active + number <= 8:
            self.active += number
        elif self.active + number <= 0:
            self.active = 8
        else:
            self.active = 0

    def change_moving(self):
        self.can_move = not self.can_move

    def change_active_in_menu(self, x):
        if 0 <= self.active_in_menu - x <= 2:
            self.active_in_menu -= x