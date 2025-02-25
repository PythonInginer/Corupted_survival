import pygame


from Player import Player
from LoadMap import generate_level
from Stick import Stick
from Flint import Flint

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


def game(map_name, main):
    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/music/Desert_theme.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    player = pygame.sprite.Group()
    player_sprite = Player()
    player_sprite.rect.x = width // 2 - 10
    player_sprite.rect.y = height // 2 - 10
    player.add(player_sprite)
    tick = 0

    ground = []
    solid_tiles_group = pygame.sprite.Group()
    ghost_tiles_group = pygame.sprite.Group()
    ground = generate_level(f'{map_name}', ghost_tiles_group, solid_tiles_group, ground)

    resources_list = []

    resources = pygame.sprite.Group()
    for i in range(10):
        stick = Stick()
        resources_list.append(stick)
        resources.add(stick)

    for i in range(10):
        flint = Flint()
        resources_list.append(flint)
        resources.add(flint)

    running = True
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_sprite.move_directions.append("left")
                if event.key == pygame.K_d:
                    player_sprite.move_directions.append("right")
                if event.key == pygame.K_w:
                    player_sprite.move_directions.append("up")
                if event.key == pygame.K_s:
                    player_sprite.move_directions.append("down")
                if event.key == pygame.K_e:
                    if len(player_sprite.inventory) < 8:
                        for i in range(len(resources_list)):
                            if player_sprite.rect.colliderect(resources_list[i].rect):
                                if player_sprite.inventory:
                                    has = False
                                    for j in range(len(player_sprite.inventory)):
                                        if resources_list[i].name == player_sprite.inventory[j][0]:
                                            player_sprite.inventory[j][1] += 1
                                            has = True
                                    if not has:
                                        player_sprite.inventory.append([resources_list[i].name, 1])
                                else:
                                    player_sprite.inventory.append([resources_list[i].name, 1])
                                del resources_list[i]

                                resources.empty()
                                for j in range(len(resources_list)):
                                    resources.add(resources_list[j])
                                break
                if event.key == pygame.K_1:
                    player_sprite.change_active(0)
                if event.key == pygame.K_2:
                    player_sprite.change_active(1)
                if event.key == pygame.K_3:
                    player_sprite.change_active(2)
                if event.key == pygame.K_4:
                    player_sprite.change_active(3)
                if event.key == pygame.K_5:
                    player_sprite.change_active(4)
                if event.key == pygame.K_6:
                    player_sprite.change_active(5)
                if event.key == pygame.K_7:
                    player_sprite.change_active(6)
                if event.key == pygame.K_8:
                    player_sprite.change_active(7)
                if event.key == pygame.K_9:
                    player_sprite.change_active(8)
                if event.key == pygame.K_ESCAPE:
                    player_sprite.change_moving()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    del player_sprite.move_directions[player_sprite.move_directions.index("left")]
                if event.key == pygame.K_d:
                    del player_sprite.move_directions[player_sprite.move_directions.index("right")]
                if event.key == pygame.K_w:
                    del player_sprite.move_directions[player_sprite.move_directions.index("up")]
                if event.key == pygame.K_s:
                    del player_sprite.move_directions[player_sprite.move_directions.index("down")]
            if not player_sprite.can_move:
                if event.type == pygame.MOUSEWHEEL:
                    player_sprite.change_active_in_menu(event.y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if player_sprite.exit_button.collidepoint(event.pos[0], event.pos[1]):
                            running = False
                            main()
                        if player_sprite.craft_button.collidepoint(event.pos[0], event.pos[1]):
                            player_sprite.craft()
            elif event.type == pygame.MOUSEWHEEL:
                player_sprite.change_active_with_mouse(event.y)

        for i in range(len(ground)):
            for j in range(len(ground[i])):
                ground[i][j].render(player_sprite)
        ghost_tiles_group.draw(screen)
        solid_tiles_group.draw(screen)

        for i in range(len(resources_list)):
            resources_list[i].render(player_sprite)
        resources.draw(screen)

        pygame.draw.rect(screen, (100, 100, 100), ((0, 0), (200, 100)))
        screen.blit(pygame.font.Font(None, 50).render('HP:100/100', True, (255, 0, 0)), (0, 0))
        screen.blit(pygame.font.Font(None, 50).render('MP:500/500', True, (0, 0, 255)), (0, 50))

        player_sprite.move(tick, solid_tiles_group)
        player.draw(screen)
        player_sprite.draw_gui(screen)

        tick = clock.tick(144)
        pygame.display.flip()

    pygame.quit()
