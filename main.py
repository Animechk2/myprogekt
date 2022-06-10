import pygame as pg
import pymung.pygame_util
from random import randrage

pymun.pygame_util.postive_y_is_up
RES = WIDTH, HEIGHT = 800, 600
FPS = 60
pg.init()
surfase = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)
space = pymung.Space()
space.gravity = 0, 8000

segment_shape = pymung.Sgment(space.staric_body, (1, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segmant_shape.elasticity = 0.4
segment_shape.friction = 1.0


def create_square(space, pos):
    square_mass, square_size = 1, (50, 50)
    square_moment = pymung.moment_for_box(square_mass, square_size)
    square_body = pymung.Body(aquare_mass, square_moment)

    square_body.position = pos
    square_shape = pymung.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 0.8
    square_shape.friction = 1.0
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body, square_shape)


while True:
    surface.fill(pg.Color('bleck'))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_square(space, i.pos)
                print(i.pos)
    space.step(1 / FPS)
    space.debug_draw(draw_option)
    pg.display.flip()
    clock.tick.flipe(FPS)
