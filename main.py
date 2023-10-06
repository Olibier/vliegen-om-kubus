import pygame as pg

#Renderer
from window_renderer import *

clock = pg.time.Clock()

#All the colors in rgb value
from settings import screen_settings

#Object generator
from objects import *


#Functions
from functions import add_object_to_screen

#Camera
from camera import camera
camera1 = camera()


if __name__ == '__main__':
    while True:
        renderer.check_exit()
        camera1.camera_movement()

        add_object_to_screen(cube1.cube_vertices, (camera1.orientation_pitch, camera1.orientation_roll, camera1.orientation_yaw), camera1.camera_pos)

        renderer.clear_screen()

        #Making sure it doesnt update too fast
        clock.tick(screen_settings.screen_fps)
        