import numpy as np
import math

class cube():
    def __init__(self, size, center_position):
        self.size = size
        self.half_size = size/2
        self.center_position = center_position

        self.points = [(center_position[0] - self.half_size, center_position[1] - self.half_size, center_position[2] - self.half_size),
                       (center_position[0] - self.half_size, center_position[1] + self.half_size, center_position[2] - self.half_size),
                       (center_position[0] + self.half_size, center_position[1] + self.half_size, center_position[2] - self.half_size),
                       (center_position[0] + self.half_size, center_position[1] - self.half_size, center_position[2] - self.half_size),
                    
                       (center_position[0] - self.half_size, center_position[1] - self.half_size, center_position[2] + self.half_size),
                       (center_position[0] - self.half_size, center_position[1] + self.half_size, center_position[2] + self.half_size),
                       (center_position[0] + self.half_size, center_position[1] + self.half_size, center_position[2] + self.half_size),
                       (center_position[0] + self.half_size, center_position[1] - self.half_size, center_position[2] + self.half_size)]
        
        self.lines = [(self.points[0], self.points[1]),
                      (self.points[1], self.points[2]),
                      (self.points[2], self.points[3]),
                      (self.points[3], self.points[0]),
                      
                      (self.points[4], self.points[5]),
                      (self.points[5], self.points[6]),
                      (self.points[6], self.points[7]),
                      (self.points[7], self.points[4]),
                      
                      (self.points[0], self.points[4]),
                      (self.points[1], self.points[5]),
                      (self.points[2], self.points[6]),
                      (self.points[3], self.points[7]),]
    
    def rotate_cube_y(self, degrees):
        radians = np.radians(degrees)
        rotated_cube_points = []
        for point in self.points:
            point_matrix = np.matrix([[point[0]],
                                      [point[1]],
                                      [point[2]]])
            rotate_y_axis_matrix = np.matrix([[math.cos(radians), 0, math.sin(radians)],
                                              [0, 1, 0],
                                              [-math.sin(radians), 0, math.cos(radians)]])
            
            rotated_point_matrix = rotate_y_axis_matrix * point_matrix
            rotated_point_tolist = rotated_point_matrix.tolist()

            rotated_cube_points.append((rotated_point_tolist[0][0], rotated_point_tolist[1][0], rotated_point_tolist[2][0]))
        self.points = rotated_cube_points
        self.lines = [(self.points[0], self.points[1]),
                      (self.points[1], self.points[2]),
                      (self.points[2], self.points[3]),
                      (self.points[3], self.points[0]),
                      
                      (self.points[4], self.points[5]),
                      (self.points[5], self.points[6]),
                      (self.points[6], self.points[7]),
                      (self.points[7], self.points[4]),
                      
                      (self.points[0], self.points[4]),
                      (self.points[1], self.points[5]),
                      (self.points[2], self.points[6]),
                      (self.points[3], self.points[7]),]
