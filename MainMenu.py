import pygame
import pygame_gui
import sys


def text_creator(txt, screen, size, color=(0, 0, 0), xy=(0, 0), font=None, smoothing=False):
    text_parameter = pygame.font.Font(font, size)
    text = text_parameter.render(txt, smoothing, color)
    screen.blit(text, xy)


class MainMenu:
    def __init__(self, manager, w, h, screen):
        self.manager = manager
        self.w = w
        self.h = h
        self.screen = screen
        btn_size_x = 220
        w_center = (self.w - btn_size_x) // 2

        self.single_player_btn = self.create_btn(w_center,
                                                 (self.h - 50) // 2 - 120, btn_size_x, 50, 'Одиночная игра')
        self.multi_player_btn = self.create_btn(w_center,
                                                (self.h - 50) // 2 - 60, btn_size_x, 50, 'Многопользовательская игра')
        self.settings_btn = self.create_btn(w_center,
                                            (self.h - 50) // 2, btn_size_x, 50, 'Настройки')
        self.exit_btn = self.create_btn(w_center,
                                        (self.h - 50) // 2 + 60, btn_size_x, 50, 'Выход')

    def create_btn(self, x, y, w, h, txt):
        btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (w, h)),
            text=f'{txt}',
            manager=self.manager,

        )
        return btn

    def detect(self, ui_el, sections):
        sp, mp, st = sections
        if ui_el == self.single_player_btn:
            self.hide_all()
            sp.show_all()
            return 1
        if ui_el == self.multi_player_btn:
            self.hide_all()
            mp.show_all()
            mp.always_show()
            return 2
        if ui_el == self.settings_btn:
            self.hide_all()
            st.show_all()
            return 3
        if ui_el == self.exit_btn:
            sys.exit()

    def hide_all(self):
        self.single_player_btn.hide()
        self.multi_player_btn.hide()
        self.settings_btn.hide()
        self.exit_btn.hide()

    def show_all(self):
        self.single_player_btn.show()
        self.multi_player_btn.show()
        self.settings_btn.show()
        self.exit_btn.show()

    def always_show(self):
        text_creator('Заражённый мир', self.screen, 120, (0, 0, 0), (720, 100), 'data/fonts/cursed.ttf', True)
        text_creator('alpha V 0.0.8.7', self.screen, 30, (0, 0, 0), (20, 1060), None, True)


class SinglePlayer:
    def __init__(self, manager, screen):
        super().__init__()
        self.manager = manager
        self.screen = screen

        self.back_btn = self.create_btn(20, 20, 100, 40, '<--')
        self.create_world_btn = self.create_btn(1525, 980, 150, 60, 'создать')
        self.continue_btn = self.create_btn(1700, 980, 150, 60, 'продолжить')

        self.create_worlds_menu()

        self.world_name = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((700, 350), (200, 40)),
            manager=self.manager
        )

        self.hide_all()

    def create_btn(self, x, y, w, h, txt):
        btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (w, h)),
            text=f'{txt}',
            manager=self.manager
        )
        return btn

    def hide_all(self):
        self.back_btn.hide()
        self.create_world_btn.hide()
        self.continue_btn.hide()
        self.worlds.hide()
        self.world_name.hide()

    def show_all(self):
        self.back_btn.show()
        self.create_world_btn.show()
        self.continue_btn.show()
        self.worlds.show()
        self.world_name.show()

    def create_worlds_menu(self):
        worlds = open('data/maps_names.txt', 'r').read().split()
        self.worlds = pygame_gui.elements.UIDropDownMenu(
            options_list=worlds,
            starting_option=worlds[0],
            manager=self.manager,
            relative_rect=pygame.Rect((700, 400), (600, 100)),
            expansion_height_limit=300
        )

    def btn_press_detection(self, ui_el, main):
        if ui_el == self.back_btn:
            self.hide_all()
            main.show_all()
            return 0, True, 'map.txt'
        if ui_el == self.continue_btn:
            map_name = self.worlds.selected_option
            return 1, False, f'map.txt'
        if ui_el == self.create_world_btn:
            with open('data/maps_names.txt', 'a', encoding='utf8') as file:
                file.write(self.world_name.text + '\n')
            self.world_name.set_text('')
            self.worlds.kill()
            self.create_worlds_menu()
            return 1, True, 'map.txt'
        else:
            return 1, True, 'map.txt'

    def always_show(self):
        text_creator('Одиночная игра', self.screen, 120, (0, 0, 0), (720, 100), 'data/fonts/cursed.ttf', True)


class MultiPlayer:
    def __init__(self, manager, screen):
        super().__init__()
        self.manager = manager
        self.screen = screen

        self.back_btn = self.create_btn(20, 20, 100, 40, '<--')

        self.hide_all()

    def create_btn(self, x, y, w, h, txt):
        btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (w, h)),
            text=f'{txt}',
            manager=self.manager
        )
        return btn

    def hide_all(self):
        self.back_btn.hide()

    def show_all(self):
        self.back_btn.show()

    def btn_press_detection(self, ui_el, main):
        if ui_el == self.back_btn:
            self.hide_all()
            main.show_all()
            return 0

    def always_show(self):
        text_creator('В ДОРАБОТКЕ, возвращайтесь позже =)', self.screen, 80, (0, 0, 0), (400, 470), None, True)


class Settings:
    def __init__(self, manager, screen):
        super().__init__()
        self.manager = manager
        self.screen = screen

        self.back_btn = self.create_btn(20, 20, 100, 40, '<--')

        self.hide_all()

    def create_btn(self, x, y, w, h, txt):
        btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (w, h)),
            text=f'{txt}',
            manager=self.manager
        )
        return btn

    def hide_all(self):
        self.back_btn.hide()

    def show_all(self):
        self.back_btn.show()

    def btn_press_detection(self, ui_el, main):
        if ui_el == self.back_btn:
            self.hide_all()
            main.show_all()
            return 0

    def always_show(self):
        text_creator('Настройки', self.screen, 120, (0, 0, 0), (720, 100), 'data/fonts/cursed.ttf', True
                     )
        text_creator('О разработчиках', self.screen, 100, (0, 0, 0), (300, 400), 'data/fonts/cursed.ttf', True
                     )
        text_creator('By GrayBreadCompany', self.screen, 65, (0, 0, 0), (300, 540), 'data/fonts/cursed.ttf', True
                     )
        text_creator('Нечетов Глеб - Программист', self.screen, 45, (0, 0, 0), (300, 600), 'data/fonts/cursed.ttf', True
                     )
        text_creator('Савченко Сергей - Программист', self.screen, 45, (0, 0, 0), (300, 650), 'data/fonts/cursed.ttf',
                     True
                     )
        text_creator('Хаустов Михаил - Художник, Sound-дизайнер', self.screen, 45, (0, 0, 0), (300, 700),
                     'data/fonts/cursed.ttf', True
                     )
