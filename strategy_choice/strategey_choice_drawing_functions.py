import general_functions.colors as cl
import general_functions.pygame_functions as pyf
import general_functions.images_functions as imf
import strategy_choice.strategy_choice_constants as const
import pygame

WIDTH, HEIGHT, FPS = const.get_constants()


def draw_everything_in_strategy_choice_stage(screen, mouse_location, armies):
    screen.fill(cl.BLUE)
    draw_background(screen)
    draw_strategy_choice_text(screen)
    draw_armies(armies, screen)
    # draw_deployment(deployment, screen)
    pyf.draw_mouse(screen, mouse_location)


def draw_armies(armies, screen):
    for army in armies:
        if army.am_i_enemy_team:
            draw_enemy_army_units(army, screen)
        else:
            draw_player_army_units(army, screen)


def draw_enemy_army_units(army, screen):
    if len(army.unit_list) > 0:
        for unit in army.unit_list:
            if unit.exposed:
                unit_image, unit_rect = get_enemy_unit_graphic_details(unit)
                screen.blit(unit_image, unit_rect)


def draw_player_army_units(army, screen):
    if len(army.unit_list) > 0:
        for unit in army.unit_list:
            unit_image, unit_rect = get_unit_graphic_details(unit)
            screen.blit(unit_image, unit_rect)


def get_unit_graphic_details(unit):
    unit_image = get_unit_image(unit)
    unit_rect = get_unit_rect(unit, unit_image)
    return unit_image, unit_rect


def get_enemy_unit_graphic_details(unit):
    unit_image = get_enemy_unit_image(unit)
    unit_rect = get_unit_rect(unit, unit_image)
    return unit_image, unit_rect


def get_enemy_unit_image(unit):
    unit_path = 'sprites/' + str(unit.type) + '_red_mark.png'
    unit_image = pygame.image.load(unit_path)
    unit_image.set_colorkey(cl.COLOR_KEY)
    return unit_image


def get_unit_image(unit):
    unit_path = 'sprites/' + str(unit.type) + '.png'
    unit_image = pygame.image.load(unit_path)
    unit_image.set_colorkey(cl.COLOR_KEY)
    return unit_image


def get_unit_rect(unit, unit_image):
    unit_rect = unit_image.get_rect()
    unit_rect.x = 20 + (unit.x_position - 1) * 120
    unit_rect.y = 150 + unit.y_position * 60
    return unit_rect


def draw_strategy_choice_text(screen):
    draw_the_head_line(screen)


def draw_the_head_line(screen):
    title_text, title_rect = imf.get_text_stats("Command your troops", 60, cl.WHITE, [360, 40])
    imf.draw_titles(screen, [title_text, title_rect])


def draw_background(screen):
    starting_y = 180
    draw_background_rectangle(screen, starting_y)
    draw_background_lines(screen, starting_y)


def draw_background_rectangle(screen, starting_y):
    pygame.draw.rect(screen, cl.GREEN, (0, starting_y, 720, 360))  # (x, y, width, height)
    pygame.draw.rect(screen, cl.GREY, (360, starting_y, 720, 360))  # (x, y, width, height)


def draw_background_lines(screen, starting_y):
    for i in range(5):
        if (120 + i * 120) < 360:
            color = cl.DARK_BROWN
            size = 2
        elif (120 + i * 120) == 360:
            color = cl.BLACK
            size = 5
        else:
            color = cl.DARK_GREY
            size = 2
        pygame.draw.line(screen, color, (120 + 120 * i, starting_y), (120 + 120 * i, HEIGHT),
                         size)  # (start_pos), (end_pos), width
