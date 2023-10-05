import pygame
import numpy
import sys
import math
import keyboard

#Pygame
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#(x, y, z)
cube = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]

#Display Surface Settings
display_surface_distance_to_camera = 10
display_x_relative_to_camera = 0
display_y_relative_to_camera = 0

cam_x = 0
cam_y = 0
cam_z = -10

empty_lista = []

cam_pitch = 0
cam_roll = 0
cam_yaw = 0

cam_movement_speed = 0.1

def check_if_facing_point(camera_orientation, camera_pos, point):
    check_movement_speed = 1
    dummy_check_camera_x = camera_pos[0]
    dummy_check_camera_y = camera_pos[1]
    dummy_check_camera_z = camera_pos[2]

    current_camera_distance = numpy.sqrt((point[0] - camera_pos[0])**2 + (point[1] - camera_pos[1])**2 + (point[2] - camera_pos[2])**2)

    dx = math.sin(camera_orientation[1]) * math.cos(camera_orientation[0]) * check_movement_speed
    dy = -math.sin(camera_orientation[0]) * check_movement_speed
    dz = math.cos(camera_orientation[0]) * math.cos(camera_orientation[1]) * check_movement_speed

    dummy_check_camera_x += dx
    dummy_check_camera_y += dy
    dummy_check_camera_z += dz

    dummy_check_camera = (dummy_check_camera_x, dummy_check_camera_y, dummy_check_camera_z)

    dummy_camera_distance = numpy.sqrt((point[0] - dummy_check_camera[0])**2 + (point[1] - dummy_check_camera[1])**2 + (point[2] - dummy_check_camera[2])**2)

    return current_camera_distance > dummy_camera_distance

def draw_on_pygame_screen(pointXY, screen_width, screen_height, x_max, y_max):
    point_x = pointXY[0]
    point_y = pointXY[1]

    x_pygame = screen_width/2 + ((1/x_max) * point_x) * screen_width/2
    y_pygame = screen_height/2 - ((1/y_max) * point_y) * screen_height/2

    return (x_pygame, y_pygame)

def projection_matrix(points_to_project, camera_pos, camera_orientation):
    empty_list = []
    for point in points_to_project:
        camera_x = camera_pos[0]
        camera_y = camera_pos[1]
        camera_z = camera_pos[2]

        point_x = point[0]
        point_y = point[1]
        point_z = point[2]

        camera_orientation_x = camera_orientation[0]
        camera_orientation_y = camera_orientation[1]
        camera_orientation_z = camera_orientation[2]

        point_to_project_matrix = numpy.matrix([[point_x],
                                                [point_y],
                                                [point_z]])
        
        camera_pos_matrix = numpy.matrix([[camera_x],
                                          [camera_y],
                                          [camera_z]])
        
        orientationx_matrix = numpy.matrix([[1, 0, 0],
                                            [0, math.cos(camera_orientation_x), math.sin(camera_orientation_x)],
                                            [0, -math.sin(camera_orientation_x), math.cos(camera_orientation_x)]])
        
        orientationy_matrix = numpy.matrix([[math.cos(camera_orientation_y), 0, -math.sin(camera_orientation_y)],
                                            [0, 1, 0],
                                            [math.sin(camera_orientation_y), 0, math.cos(camera_orientation_y)]])
        
        orientationz_matrix = numpy.matrix([[math.cos(camera_orientation_z), math.sin(camera_orientation_z), 0],
                                            [-math.sin(camera_orientation_z), math.cos(camera_orientation_z), 0],
                                            [0, 0, 1]])
        
        dXYZ_matrix = orientationx_matrix * orientationy_matrix * orientationz_matrix * (point_to_project_matrix - camera_pos_matrix)
        dXYZ = dXYZ_matrix.tolist()

        dX = dXYZ[0][0]
        dY = dXYZ[1][0]
        dZ = dXYZ[2][0]

        projected_x = (display_surface_distance_to_camera/dZ)*dX + display_x_relative_to_camera
        projected_y = (display_surface_distance_to_camera/dZ)*dY + display_y_relative_to_camera

        empty_list.append((projected_x, projected_y))

    return empty_list

while True:
    empty_lista = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)

    cam_orientation = (cam_pitch, cam_roll, cam_yaw)

    if keyboard.is_pressed('w'):
        dx = math.sin(cam_roll) * math.cos(cam_pitch) * cam_movement_speed
        dy = -math.sin(cam_pitch) * cam_movement_speed
        dz = math.cos(cam_pitch) * math.cos(cam_roll) * cam_movement_speed

        cam_x += dx
        cam_y += dy
        cam_z += dz

    if keyboard.is_pressed('s'):
        dx = -math.sin(cam_roll) * math.cos(cam_pitch) * cam_movement_speed
        dy = math.sin(cam_pitch) * cam_movement_speed
        dz = -math.cos(cam_pitch) * math.cos(cam_roll) * cam_movement_speed
        
        cam_x += dx
        cam_y += dy
        cam_z += dz
    
    if keyboard.is_pressed('a'):
        dx = -math.cos(cam_roll) * cam_movement_speed
        dy = 0
        dz = math.sin(cam_roll) * cam_movement_speed

        cam_x += dx
        cam_y += dy
        cam_z += dz

    if keyboard.is_pressed('d'):
        dx = math.cos(cam_roll) * cam_movement_speed
        dy = 0
        dz = -math.sin(cam_roll) * cam_movement_speed

        cam_x += dx
        cam_y += dy
        cam_z += dz

    if keyboard.is_pressed('up arrow'):
        cam_pitch -= 0.01
    if keyboard.is_pressed('down arrow'):
        cam_pitch += 0.01
    if keyboard.is_pressed('right arrow'):
        cam_roll += 0.01
    if keyboard.is_pressed('left arrow'):
        cam_roll -= 0.01
        

    for point in cube:
        if check_if_facing_point(cam_orientation, (cam_x, cam_y, cam_z), point):
            empty_lista.append(point)

    print(empty_lista)

    cube_projected = projection_matrix(empty_lista, (cam_x, cam_y, cam_z), cam_orientation)

    for point in cube_projected:
        pygame.draw.circle(screen, BLACK, draw_on_pygame_screen(point, screen_width, screen_height, 5, 5), 2)

    pygame.display.flip()
    clock.tick(120)

