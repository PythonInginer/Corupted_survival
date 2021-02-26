import sys
import pygame
from random import randint

lvl_name = 'map.txt'

pygame.init()
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

TILE_WH = 75
FPS = 50
clock = pygame.time.Clock()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, rotate):
        super().__init__(all_sprites)

        im, ghost_solid = tile_images[tile_type]

        for i in range(randint(1, 3) if rotate == 4 else int(rotate)):
            im = pygame.transform.rotate(im, 90)
        if ghost_solid == 'ghost':
            ghost_tiles_group.add(self)
        elif ghost_solid == 'solid':
            solid_tiles_group.add(self)

        self.image = im
        self.rect = self.image.get_rect().move(TILE_WH * pos_x, TILE_WH * pos_y)


class LoadMap:
    def load_image(self, name):
        image = pygame.image.load(f'textures/{name}').convert()
        image = image.convert_alpha()
        image = pygame.transform.scale(image, (TILE_WH, TILE_WH))
        return image

    def generate_level(self, level):
        new_player, x, y = None, None, None
        level = self.load_level(level)
        for y in range(len(level)):
            for x in range(len(level[y])):
                tile_type, rotate = level[y][x].split('_')
                Tile(tile_type, x, y, int(rotate))
        return x, y

    def load_level(self, filename):
        filename = "data/" + filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip().split() for line in mapFile]
        return level_map


all_sprites = pygame.sprite.Group()
solid_tiles_group = pygame.sprite.Group()
ghost_tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

lm = LoadMap()

tile_images = {
    'sandY1': (lm.load_image('dirt.jpg'), 'ghost'),
    'DtGraB': (lm.load_image('DirtGrassBot.jpg'), 'ghost'),
    'DtGraR': (lm.load_image('DirtGrassRight.jpg'), 'ghost'),
    'DtGrBR': (lm.load_image('DirtGrassBotRight.jpg'), 'ghost'),
    'DtGrTL': (lm.load_image('DirtGrassTopLeft.jpg'), 'ghost'),
    'DtGrBL': (lm.load_image('DirtGrassBotLeft.jpg'), 'ghost'),
    'DtGrTR': (lm.load_image('DirtGrassTopRight.jpg'), 'ghost'),
    'InfCW1': (lm.load_image('InfectCommonWater1.jpg'), 'ghost'),
    'InfCW2': (lm.load_image('InfectCommonWater2.jpg'), 'ghost'),
    'InfSt1': (lm.load_image('InfectStone1.jpg'), 'ghost'),
    'InfSt2': (lm.load_image('InfectStone2.jpg'), 'ghost'),
    'InfSt3': (lm.load_image('InfectStone3.jpg'), 'ghost'),
    'InfWt1': (lm.load_image('InfectWater1.jpg'), 'solid'),
    'InfWt2': (lm.load_image('InfectWater2.jpg'), 'solid'),
    'InfWt3': (lm.load_image('InfectWater3.jpg'), 'solid'),
    'InfWt4': (lm.load_image('InfectWater4.jpg'), 'solid'),
    'nigSt1': (lm.load_image('nightStone1.jpg'), 'ghost'),
    'nigSt2': (lm.load_image('nightStone2.jpg'), 'ghost'),
    'nigSt3': (lm.load_image('nightStone3.jpg'), 'ghost'),
    'Stone1': (lm.load_image('Stone1.jpg'), 'ghost'),
    'Stone2': (lm.load_image('Stone2.jpg'), 'ghost'),
    'Stone3': (lm.load_image('Stone3.jpg'), 'ghost'),
    'grass1': (lm.load_image('grass1.jpg'), 'ghost'),
    'grass2': (lm.load_image('grass2.jpg'), 'ghost'),
    'grass3': (lm.load_image('grass3.jpg'), 'ghost'),
    'grass4': (lm.load_image('grass4.jpg'), 'ghost'),
    'Water1': (lm.load_image('Water1.jpg'), 'solid'),
    'Water2': (lm.load_image('Water2.jpg'), 'solid'),
    'Water3': (lm.load_image('Water3.jpg'), 'solid'),
    'Water4': (lm.load_image('Water4.jpg'), 'solid'),
    'InTGrB': (lm.load_image('infectTrueGrassB.jpg'), 'ghost'),
    'InTGBL': (lm.load_image('infectTrueGrassBL.jpg'), 'ghost'),
    'InTGrL': (lm.load_image('infectTrueGrassL.jpg'), 'ghost'),
    'InTGrR': (lm.load_image('infectTrueGrassR.jpg'), 'ghost'),
    'InTGrT': (lm.load_image('infectTrueGrassT.jpg'), 'ghost'),
    'InTGTR': (lm.load_image('infectTrueGrassTR.jpg'), 'ghost'),

}
level_x, level_y = lm.generate_level('map.txt')
