import pygame

from recipes import recipes
from Axe import Axe
from PickAxe import PickAxe
from Spear import Spear
from Rope import Rope
from Flint import Flint
from Stick import Stick
from CursedGrass import CursedGrass


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("data/skins/player2.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.move_directions = []
        self.field_x = 0
        self.field_y = 0

        self.inventory = []
        self.active = 0
        self.active_in_menu = 0
        self.can_move = True

        self.top_collider = pygame.Rect(1920 // 2, 1080 // 2 - 10, 55, 10)
        self.bottom_collider = pygame.Rect(1920 // 2, 1080 // 2 - 20 + self.rect.height, 55, 10)
        self.left_collider = pygame.Rect(1920 // 2 - 10, 1080 // 2 - 10, 10, 75)
        self.right_collider = pygame.Rect(1920 // 2 - 20 + self.rect.width, 1080 // 2 - 10, 10, 75)

        self.k = 0

    def move(self, tick, solid_tiles_group):
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

            for i in solid_tiles_group:
                if self.top_collider.colliderect(i.rect):
                    self.field_y += self.step
                elif self.bottom_collider.colliderect(i.rect):
                    self.field_y += -self.step
                elif self.left_collider.colliderect(i.rect):
                    self.field_x += self.step
                elif self.right_collider.colliderect(i.rect):
                    self.field_x += -self.step

    def draw_gui(self, screen):
        k = 0
        for i in range(9):
            if i == self.active:
                pygame.draw.rect(screen, "white", (100 * i + 200, 980, 100, 100), 6)
            else:
                pygame.draw.rect(screen, "white", (100 * i + 200, 980, 100, 100), 1)
        for i in range(len(self.inventory)):
            temp = pygame.sprite.Group()
            if self.inventory[i][0] == "flint":
                sprite = Flint()
            elif self.inventory[i][0] == "stick":
                sprite = Stick()
            elif self.inventory[i][0] == "axe":
                sprite = Axe()
            elif self.inventory[i][0] == "pickaxe":
                sprite = PickAxe()
            elif self.inventory[i][0] == "rope":
                sprite = Rope()
            sprite.rect.x = 100 * k + 200
            sprite.rect.y = 980
            font = pygame.font.Font(None, 50)
            text = font.render(str(self.inventory[i][1]), True, (100, 255, 100))
            screen.blit(text, (100 * k + 200, 1030))
            temp.add(sprite)
            temp.draw(screen)
            temp.empty()
            k += 1

        if not self.can_move:
            for i in range(3):
                if i == self.active_in_menu:
                    pygame.draw.rect(screen, "white", (10, 100 * i + 100, 100, 100), 6)
                else:
                    pygame.draw.rect(screen, "white", (10, 100 * i + 100, 100, 100), 1)

            o = self.k + 3
            self.group = pygame.sprite.Group()
            self.recipes_list = list(recipes)
            flag = True
            h = 0
            for i in range(self.k, o):
                if 100 <= 100 * self.k + 100 <= 300:
                    if self.recipes_list[i] == "axe":
                        sprite = Axe()
                    elif self.recipes_list[i] == "pickaxe":
                        sprite = PickAxe()
                    elif self.recipes_list[i] == "spear":
                        sprite = Spear()
                    elif self.recipes_list[i] == "rope":
                        sprite = Rope()
                if flag:
                    for j in recipes.keys():
                        if j == self.recipes_list[self.active_in_menu + self.k]:
                            for k in recipes[j]:
                                pygame.draw.rect(screen, "white", ((120 * h * 0.6 + 120,
                                                                    100 * self.active_in_menu + 100),
                                                                   (50, 50)), 1)
                                if k == "flint":
                                    sprite2 = Flint()
                                    sprite2.rect.x = 120 * h * 0.6 + 120
                                    sprite2.rect.y = 100 * self.active_in_menu + 100
                                elif k == "stick":
                                    sprite2 = Stick()
                                    sprite2.rect.x = 120 * h * 0.6 + 120
                                    sprite2.rect.y = 100 * self.active_in_menu + 100
                                elif k == "rope":
                                    sprite2 = Rope()
                                    sprite2.rect.x = 120 * h * 0.6 + 120
                                    sprite2.rect.y = 100 * self.active_in_menu + 100
                                elif k == "cursed_grass":
                                    sprite2 = CursedGrass()
                                    sprite2.rect.x = 120 * h * 0.6 + 120
                                    sprite2.rect.y = 100 * self.active_in_menu + 100
                                self.group.add(sprite2)
                                print()
                                h += 1
                    flag = False
                sprite.rect.x = 10
                sprite.rect.y = 100 * (i - self.k) + 100
                self.group.add(sprite)
            self.group.draw(screen)

            self.craft_button = pygame.Rect(150, 300, 250, 80)
            font = pygame.font.Font(None, 50)
            text = font.render("Создать", True, (0, 0, 0))
            screen.blit(text, (150, 400))

            self.exit_button = pygame.Rect(1600, 1000, 320, 80)
            font = pygame.font.Font(None, 50)
            text = font.render("Выйти в меню", True, (0, 0, 0))
            screen.blit(text, (1600, 1000))

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
        if -1 <= self.active_in_menu - x <= 3:
            self.active_in_menu -= x
        if 0 <= self.k - x <= 1 and (self.active_in_menu == 3 or self.active_in_menu == -1):
            self.active_in_menu = 0
            self.k -= x
        if (self.active_in_menu == 3 or self.active_in_menu == -1) and self.k == 1:
            self.active_in_menu = 2
        if (self.active_in_menu == 3 or self.active_in_menu == -1) and self.k == 0:
            self.active_in_menu = 0

    def craft(self):
        count = 0
        for i in recipes[self.recipes_list[self.active_in_menu + self.k]]:
            for j in range(len(self.inventory)):
                if i == self.inventory[j][0]:
                    if recipes[self.recipes_list[self.active_in_menu + self.k]][i] <= self.inventory[j][1]:
                        count += 1
        if count == len(recipes[self.recipes_list[self.active_in_menu + self.k]]):
            for i in recipes[self.recipes_list[self.active_in_menu + self.k]]:
                for j in range(len(self.inventory)):
                    if i == self.inventory[j][0]:
                        if recipes[self.recipes_list[self.active_in_menu + self.k]][i] <= self.inventory[j][1]:
                            self.inventory[j][1] -= recipes[self.recipes_list[self.active_in_menu + self.k]][i]
            self.inventory.append([self.recipes_list[self.active_in_menu + self.k], 1])
        for i in range(len(self.inventory) - 1, -1, -1):
            if self.inventory[i][1] == 0:
                del self.inventory[i]