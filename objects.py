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