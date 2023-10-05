import pygame as pg

#Renderer
from window_renderer import window_renderer
renderer = window_renderer()
clock = pg.time.Clock()

#All the colors in rgb value
from settings import colors, screen_settings, camera_settings

#Object generator
from objects import cube
cube1 = cube(1, (0, 0, 0))

#Math
import math_formulas

#Camera
from camera import camera
camera1 = camera()


if __name__ == '__main__':
    while True:
        renderer.check_exit()
        camera1.camera_movement()
        cube1p = math_formulas.calculate_xyz_position_object_vertices(cube1.cube_vertices, (camera1.orientation_pitch, camera1.orientation_roll, camera1.orientation_yaw), camera1.camera_pos)
        cube1b = math_formulas.projection_matrix(cube1p, camera_settings.display_surface_position)
        cube1G = math_formulas.pygame_screen_xy_conversion(cube1b, screen_settings.screen_width, screen_settings.screen_height, 5, 5)

        renderer.clear_screen()

        for point in cube1G:
            renderer.draw_dot(point, (0, 0, 0), 10)
        
        
        

        #Making sure it doesnt update too fast
        clock.tick(screen_settings.screen_fps)
        print(clock.get_fps())
        