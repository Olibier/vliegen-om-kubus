class cube():
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.half_size = size/2

        self.cube_vertices = [(position[0] - self.half_size, position[1] - self.half_size, position[2] - self.half_size),
                              (position[0] - self.half_size, position[1] + self.half_size, position[2] - self.half_size),
                              (position[0] + self.half_size, position[1] + self.half_size, position[2] - self.half_size),
                              (position[0] + self.half_size, position[1] - self.half_size, position[2] - self.half_size),
                              
                              (position[0] - self.half_size, position[1] - self.half_size, position[2] + self.half_size),
                              (position[0] - self.half_size, position[1] + self.half_size, position[2] + self.half_size),
                              (position[0] + self.half_size, position[1] + self.half_size, position[2] + self.half_size),
                              (position[0] + self.half_size, position[1] - self.half_size, position[2] + self.half_size)]

        self.cube_connected_lines = [(0, 1), (1, 2), (2, 3), (3, 0),
                                     (4, 5), (5, 6), (6, 7), (7, 4),
                                     (0, 4), (3, 7), (2, 6), (1, 5)]

cube1 = cube(2, (0, 0, 0))