import numpy as np
import math

def move_camera(camera_orientation, camera_position, movement_direction_relative_orientation, movement_speed):

    camera_pitch = camera_orientation[0]
    camera_roll = camera_orientation[1]
    camera_yaw = camera_orientation[2]

    camera_x = camera_position[0]
    camera_y = camera_position[1]
    camera_z = camera_position[2]
     
    if movement_direction_relative_orientation == 'forwards':

        dx = math.sin(camera_roll) * math.cos(camera_pitch) * movement_speed
        dy = -math.sin(camera_pitch) * movement_speed
        dz = math.cos(camera_pitch) * math.cos(camera_roll) * movement_speed

        camera_x += dx
        camera_y += dy
        camera_z += dz

    if movement_direction_relative_orientation == 'backwards':

        dx = -math.sin(camera_roll) * math.cos(camera_pitch) * movement_speed
        dy = math.sin(camera_pitch) * movement_speed
        dz = -math.cos(camera_pitch) * math.cos(camera_roll) * movement_speed

        camera_x += dx
        camera_y += dy
        camera_z += dz

    if movement_direction_relative_orientation == 'left':

        dx = -math.cos(camera_roll) * movement_speed
        dy = 0
        dz = math.sin(camera_roll) * movement_speed

        camera_x += dx
        camera_y += dy
        camera_z += dz

    if movement_direction_relative_orientation == 'right':
        
        dx = math.cos(camera_roll) * movement_speed
        dy = 0
        dz = -math.sin(camera_roll) * movement_speed

        camera_x += dx
        camera_y += dy
        camera_z += dz
    
    return (camera_x, camera_y, camera_z)

def calculate_xyz_position_object_vertices(object_vertices_list, camera_orientation, camera_position):
    empty_list = []
    for point in object_vertices_list:

        aX = point[0]
        aY = point[1]
        aZ = point[2]

        cX = camera_position[0]
        cY = camera_position[1]
        cZ = camera_position[2]

        oX = camera_orientation[0]
        oY = camera_orientation[1]
        oZ = camera_orientation[2]

        dXYZ_matrix = np.matrix([[1, 0, 0], [0, math.cos(oX), math.sin(oX)], [0, -math.sin(oX), math.cos(oX)]]) * np.matrix([[math.cos(oY), 0, -math.sin(oY)], [0, 1, 0], [math.sin(oY), 0, math.cos(oY)]]) * np.matrix([[math.cos(oZ), math.sin(oZ), 0], [-math.sin(oZ), math.cos(oZ), 0], [0, 0, 1]]) * (np.matrix([[aX], [aY], [aZ]]) - np.matrix([[cX], [cY], [cZ]]))
        dXYZ = dXYZ_matrix.tolist()

        dX = dXYZ[0][0]
        dY = dXYZ[1][0]
        dZ = dXYZ[2][0]

        empty_list.append((dX, dY, dZ))
    
    return empty_list

def projection_matrix(object_vertices_list, camera_surface_position):
    empty_list = []

    for point in object_vertices_list:
        bX = (camera_surface_position[2]/point[2]) * point[0] + camera_surface_position[0]
        bY = (camera_surface_position[2]/point[2]) * point[1] + camera_surface_position[1]

        empty_list.append((bX, bY))
    
    return empty_list

def pygame_screen_xy_conversion(object_verticesXY_list, screen_width, screen_height, x_max, y_max):
    empty_list = []
    for point in object_verticesXY_list:
        point_x = point[0]
        point_y = point[1]

        x_pygame = screen_width/2 + ((1/x_max) * point_x) * screen_width/2
        y_pygame = screen_height/2 - ((1/y_max) * point_y) * screen_height/2

        empty_list.append((x_pygame, y_pygame))
    
    return empty_list