from settings import camera_settings, screen_settings
from math_formulas import *
from window_renderer import *
from objects import *

def add_object_to_screen(object, camera_orientation, camera_position):
    step1 = calculate_xyz_position_object_vertices(object, (camera_orientation[0], camera_orientation[1], camera_orientation[2]), camera_position)
    step2 = projection_matrix(step1, camera_settings.display_surface_position)
    step3 = pygame_screen_xy_conversion(step2, screen_settings.screen_width, screen_settings.screen_height, screen_settings.x_max, screen_settings.y_max)
    for point in step3:
        renderer.draw_dot(point, (0, 0, 0), 10)
    for line in cube1.cube_connected_lines:
        renderer.draw_line(step3[line[0]], step3[line[1]], (0, 0, 0))