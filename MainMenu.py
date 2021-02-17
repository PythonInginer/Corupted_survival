import pygame
import pygame_gui
import sys


class MainMenu:
    def __init__(self, manager, w, h):
        self.manager = manager
        self.w = w
        self.h = h
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
            manager=self.manager
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


class Settings:
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

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

    def close_this(self, ui_el, main):
        if ui_el == self.back_btn:
            self.hide_all()
            main.show_all()
            return None


class SinglePlayer:
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

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

    def close_this(self, ui_el, main):
        if ui_el == self.back_btn:
            self.hide_all()
            main.show_all()
            return None


class MultiPlayer:
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

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

    def close_this(self, ui_el, main):
        if ui_el == self.back_btn:
            self.hide_all()
            main.show_all()
            return None
