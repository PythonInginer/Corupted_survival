import pygame
import pygame_gui
from MainMenu import *
import sys


pygame.init()
W, H = pygame.display.Info().current_w, pygame.display.Info().current_h
FPS = 60

pygame.display.set_caption('Corupted world')  # название
screen = pygame.display.set_mode((W, H))  # объявляю дисплей

bg_im = pygame.image.load("data/bg/menu_bg.png").convert()  # подгружаю изображение
bg_im = pygame.transform.scale(bg_im, (W, H))  # ставлю его на фон

manager = pygame_gui.UIManager((W, H))

mm = MainMenu(manager, W, H, screen)  # подгружаю меню
single_player = SinglePlayer(manager, screen)
multi_player = MultiPlayer(manager, screen)
settings = Settings(manager)


clock = pygame.time.Clock()

in_main = True
select_section = None
while True:
    screen.blit(bg_im, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if in_main:
                    select_section = mm.detect(event.ui_element, (single_player, multi_player, settings))
                    in_main = False
                else:
                    if select_section == 1:
                        select_section = single_player.btn_press_detection(event.ui_element, mm)
                        if not select_section:
                            in_main = True
                    if select_section == 2:
                        select_section = multi_player.btn_press_detection(event.ui_element, mm)
                        in_main = True
                    if select_section == 3:
                        select_section = settings.btn_press_detection(event.ui_element, mm)
                        in_main = True

        manager.process_events(event)

    if select_section is None:
        mm.always_show()
    if select_section == 1:
        single_player.always_show()
    if select_section == 2:
        multi_player.always_show()
    if select_section == 3:
        pass

    manager.update(clock.tick())
    manager.draw_ui(screen)
    pygame.display.update()
    clock.tick(FPS)
