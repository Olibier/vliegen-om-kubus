from renderer import *
from camera import *
from objects import *
from world import *
from functions import *
import settings

renderer1 = renderer(settings.screen_width, settings.screen_height, settings.background_color,
                     settings.screen_fps, settings.render_color, settings.point_size, settings.line_size)

world1 = world()
camera1 = camera(settings.camera_starting_position, settings.camera_starting_orientation, settings.max_x,
                 settings.max_y, settings.movement_speed, settings.look_speed, world1)

cube1 = cube(1, (0, 0, 0))
cube2 = cube(1, (2, 0, 0))
world1.add_objects([cube1, cube2])

if __name__ == '__main__':
    while True:
        camera1.movement()
        visible_points, visible_lines = camera1.calculate_visible_xyz_points()
        pygame_xy_points, pygame_xy_points_of_lines = projection_matrix(visible_points, visible_lines, camera1.camera_orientation,
                                                                        camera1.camera_pos, settings.camera_surface_distance, settings.screen_width,
                                                                        settings.screen_height, settings.max_x, settings.max_y)
        
        cube1.rotate_cube_y(1)
        
                                    

        renderer1.update_screen(pygame_xy_points, pygame_xy_points_of_lines)

