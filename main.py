import pygame
import pygame_gui
from MainMenu import *
import Game
import sys

pygame.init()
pygame.mixer.music.load('data/music/Embient_menu.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
Klick = pygame.mixer.Sound('data/music/btn_pressed.ogg')


def main():
    pygame.mixer.music.unpause()
    W, H = pygame.display.Info().current_w, pygame.display.Info().current_h
    FPS = 60
    map_name = 'map.txt'

    pygame.display.set_caption('Corupted world')  # название
    screen = pygame.display.set_mode((W, H))  # объявляю дисплей

    bg_im = pygame.image.load("data/bg/menu_bg.jpg").convert()  # подгружаю изображение
    bg_im = pygame.transform.scale(bg_im, (W, H))  # ставлю его на фон

    manager = pygame_gui.UIManager((W, H))

    mm = MainMenu(manager, W, H, screen)  # подгружаю меню
    single_player = SinglePlayer(manager, screen)
    multi_player = MultiPlayer(manager, screen)
    settings = Settings(manager)

    clock = pygame.time.Clock()

    in_main = True
    select_section = 0
    running = True
    while running:
        screen.blit(bg_im, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    Klick.play()
                    if in_main:
                        select_section = mm.detect(event.ui_element, (single_player, multi_player, settings))
                        if select_section in (1, 2, 3):
                            in_main = False
                    else:
                        if select_section == 1:
                            select_section, running, map_name = single_player.btn_press_detection(event.ui_element, mm)
                            if select_section == 0:
                                in_main = True
                        elif select_section == 2:
                            select_section = multi_player.btn_press_detection(event.ui_element, mm)
                            if select_section == 0:
                                in_main = True
                        elif select_section == 3:
                            select_section = settings.btn_press_detection(event.ui_element, mm)
                            if select_section == 0:
                                in_main = True

            manager.process_events(event)

        if select_section == 0:
            mm.always_show()
        elif select_section == 1:
            single_player.always_show()
        elif select_section == 2:
            multi_player.always_show()
        elif select_section == 3:
            pass

        manager.update(clock.tick())
        manager.draw_ui(screen)
        pygame.display.update()
        clock.tick(FPS)

    Game.game(map_name, main)


main()
