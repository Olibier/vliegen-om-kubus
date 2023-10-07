import numpy as np
import math

def projection_matrix(xyz_points_list, xyz_lines_list, camera_orientation, camera_position, camera_surface_distance, screen_width, screen_height, x_max, y_max):
    converted_xyz_points = []
    converted_xy_points = []
    pygame_xy_points = []
    for point in xyz_points_list:

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

        converted_xyz_points.append((dX, dY, dZ))
    
    for point in converted_xyz_points:
        bX = (camera_surface_distance/point[2]) * point[0]
        bY = (camera_surface_distance/point[2]) * point[1]

        converted_xy_points.append((bX, bY))
    
    for point in converted_xy_points:
        point_x = point[0]
        point_y = point[1]

        x_pygame = screen_width/2 + ((1/x_max) * point_x) * screen_width/2
        y_pygame = screen_height/2 - ((1/y_max) * point_y) * screen_height/2

        if x_pygame < screen_width and x_pygame > 0 and y_pygame > 0 and y_pygame < screen_height:
            pygame_xy_points.append((x_pygame, y_pygame))
    


    converted_xyz_points_of_lines = []
    converted_xy_points_of_lines = []
    pygame_xy_points_of_lines = []
    
    for line in xyz_lines_list:

        point_a = line[0]
        point_b = line[1]

        aX1 = point_a[0]
        aY1 = point_a[1]
        aZ1 = point_a[2]

        aX2 = point_b[0]
        aY2 = point_b[1]
        aZ2 = point_b[2]

        cX = camera_position[0]
        cY = camera_position[1]
        cZ = camera_position[2]

        oX = camera_orientation[0]
        oY = camera_orientation[1]
        oZ = camera_orientation[2]

        dXYZ1_matrix = np.matrix([[1, 0, 0], [0, math.cos(oX), math.sin(oX)], [0, -math.sin(oX), math.cos(oX)]]) * np.matrix([[math.cos(oY), 0, -math.sin(oY)], [0, 1, 0], [math.sin(oY), 0, math.cos(oY)]]) * np.matrix([[math.cos(oZ), math.sin(oZ), 0], [-math.sin(oZ), math.cos(oZ), 0], [0, 0, 1]]) * (np.matrix([[aX1], [aY1], [aZ1]]) - np.matrix([[cX], [cY], [cZ]]))
        dXYZ1 = dXYZ1_matrix.tolist()

        dXYZ2_matrix = np.matrix([[1, 0, 0], [0, math.cos(oX), math.sin(oX)], [0, -math.sin(oX), math.cos(oX)]]) * np.matrix([[math.cos(oY), 0, -math.sin(oY)], [0, 1, 0], [math.sin(oY), 0, math.cos(oY)]]) * np.matrix([[math.cos(oZ), math.sin(oZ), 0], [-math.sin(oZ), math.cos(oZ), 0], [0, 0, 1]]) * (np.matrix([[aX2], [aY2], [aZ2]]) - np.matrix([[cX], [cY], [cZ]]))
        dXYZ2 = dXYZ2_matrix.tolist()


        dX1 = dXYZ1[0][0]
        dY1 = dXYZ1[1][0]
        dZ1 = dXYZ1[2][0]

        dX2 = dXYZ2[0][0]
        dY2 = dXYZ2[1][0]
        dZ2 = dXYZ2[2][0]

        converted_xyz_points_of_lines.append(((dX1, dY1, dZ1), (dX2, dY2, dZ2)))
    
    for line in converted_xyz_points_of_lines:

        point_a = line[0]
        point_b = line[1]

        bX1 = (camera_surface_distance/point_a[2]) * point_a[0]
        bY1 = (camera_surface_distance/point_a[2]) * point_a[1]
        bX2 = (camera_surface_distance/point_b[2]) * point_b[0]
        bY2 = (camera_surface_distance/point_b[2]) * point_b[1]

        converted_xy_points_of_lines.append(((bX1, bY1), (bX2, bY2)))
    
    for line in converted_xy_points_of_lines:

        point_a = line[0]
        point_b = line[1]

        point_x1 = point_a[0]
        point_y1 = point_a[1]

        point_x2 = point_b[0]
        point_y2 = point_b[1]

        x_pygame1 = screen_width/2 + ((1/x_max) * point_x1) * screen_width/2
        y_pygame1 = screen_height/2 - ((1/y_max) * point_y1) * screen_height/2

        x_pygame2 = screen_width/2 + ((1/x_max) * point_x2) * screen_width/2
        y_pygame2 = screen_height/2 - ((1/y_max) * point_y2) * screen_height/2

        if x_pygame1 < screen_width and x_pygame1 > 0 and y_pygame1 > 0 and y_pygame1 < screen_height or x_pygame2 < screen_width and x_pygame2 > 0 and y_pygame2 > 0 and y_pygame2 < screen_height:
            pygame_xy_points_of_lines.append(((x_pygame1, y_pygame1), (x_pygame2, y_pygame2)))

        
        
    
    return pygame_xy_points, pygame_xy_points_of_lines
    
