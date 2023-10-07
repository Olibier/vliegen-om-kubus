import math
import numpy as np
import keyboard
import settings

class camera():
    def __init__(self, camera_starting_pos, camera_starting_orientation, max_x, max_y, movement_speed, look_speed, world):
        self.camera_pos_x = camera_starting_pos[0]
        self.camera_pos_y = camera_starting_pos[1]
        self.camera_pos_z = camera_starting_pos[2]

        self.camera_pos = camera_starting_pos

        self.camera_pitch = camera_starting_orientation[0]
        self.camera_roll = camera_starting_orientation[1]
        self.camera_yaw = camera_starting_orientation[2]

        self.camera_orientation = camera_starting_orientation

        self.camera_max_x = max_x
        self.camera_max_y = max_y

        self.camera_movement_speed = movement_speed
        self.camera_look_speed = look_speed

        self.world = world
    
    def movement(self):
        if keyboard.is_pressed(settings.forwards_key):
            dx = math.sin(self.camera_roll) * math.cos(self.camera_pitch) * self.camera_movement_speed
            dy = -math.sin(self.camera_pitch) * self.camera_movement_speed
            dz = math.cos(self.camera_pitch) * math.cos(self.camera_roll) * self.camera_movement_speed

            self.camera_pos_x += dx
            self.camera_pos_y += dy
            self.camera_pos_z += dz

        if keyboard.is_pressed(settings.backwards_key):
            dx = -math.sin(self.camera_roll) * math.cos(self.camera_pitch) * self.camera_movement_speed
            dy = math.sin(self.camera_pitch) * self.camera_movement_speed
            dz = -math.cos(self.camera_pitch) * math.cos(self.camera_roll) * self.camera_movement_speed

            self.camera_pos_x += dx
            self.camera_pos_y += dy
            self.camera_pos_z += dz

        if keyboard.is_pressed(settings.left_key):

            dx = -math.cos(self.camera_roll) * self.camera_movement_speed
            dy = 0
            dz = math.sin(self.camera_roll) * self.camera_movement_speed
            
            self.camera_pos_x += dx
            self.camera_pos_y += dy
            self.camera_pos_z += dz
        
        if keyboard.is_pressed(settings.right_key):
            dx = math.cos(self.camera_roll) * self.camera_movement_speed
            dy = 0
            dz = -math.sin(self.camera_roll) * self.camera_movement_speed

            self.camera_pos_x += dx
            self.camera_pos_y += dy
            self.camera_pos_z += dz
        
        if self.camera_pitch > np.radians(-90):
            if keyboard.is_pressed(settings.look_up_key):
                self.camera_pitch -= self.camera_look_speed
    
        if self.camera_pitch < np.radians(90):
            if keyboard.is_pressed(settings.look_down_key):
                self.camera_pitch += self.camera_look_speed

        if keyboard.is_pressed(settings.look_right_key):
            self.camera_roll += self.camera_look_speed

        if keyboard.is_pressed(settings.look_left_key):
            self.camera_roll -= self.camera_look_speed

        if self.camera_roll >= np.radians(360):
            self.camera_roll = 0
        if self.camera_roll <= np.radians(-360):
            self.camera_roll = 0
        
        self.camera_pos = (self.camera_pos_x, self.camera_pos_y, self.camera_pos_z)
        self.camera_orientation = (self.camera_pitch, self.camera_roll, self.camera_yaw)
    
    def calculate_visible_xyz_points(self):
        visible_points = []
        visible_lines = []

        for object in self.world.world_objects:

            for line in object.lines:
                point_a = line[0]
                point_b = line[1]

                dummy_check_camera_x = self.camera_pos_x
                dummy_check_camera_y = self.camera_pos_y
                dummy_check_camera_z = self.camera_pos_z

                current_camera_distance_point_a = np.sqrt((point_a[0] - self.camera_pos_x)**2 + (point_a[1] - self.camera_pos_y)**2 + (point_a[2] - self.camera_pos_z)**2)
                current_camera_distance_point_b = np.sqrt((point_b[0] - self.camera_pos_x)**2 + (point_b[1] - self.camera_pos_y)**2 + (point_b[2] - self.camera_pos_z)**2)

                dx = math.sin(self.camera_orientation[1]) * math.cos(self.camera_orientation[0])
                dy = -math.sin(self.camera_orientation[0])
                dz = math.cos(self.camera_orientation[0]) * math.cos(self.camera_orientation[1])

                dummy_check_camera_x += dx
                dummy_check_camera_y += dy
                dummy_check_camera_z += dz

                dummy_check_camera = (dummy_check_camera_x, dummy_check_camera_y, dummy_check_camera_z)

                dummy_camera_distance_a = np.sqrt((point_a[0] - dummy_check_camera[0])**2 + (point_a[1] - dummy_check_camera[1])**2 + (point_a[2] - dummy_check_camera[2])**2)
                dummy_camera_distance_b = np.sqrt((point_b[0] - dummy_check_camera[0])**2 + (point_b[1] - dummy_check_camera[1])**2 + (point_b[2] - dummy_check_camera[2])**2)

                if current_camera_distance_point_a > dummy_camera_distance_a or current_camera_distance_point_b > dummy_camera_distance_b:
                    visible_lines.append((point_a, point_b))

            for point in object.points:
                dummy_check_camera_x = self.camera_pos_x
                dummy_check_camera_y = self.camera_pos_y
                dummy_check_camera_z = self.camera_pos_z

                current_camera_distance = np.sqrt((point[0] - self.camera_pos_x)**2 + (point[1] - self.camera_pos_y)**2 + (point[2] - self.camera_pos_z)**2)

                dx = math.sin(self.camera_orientation[1]) * math.cos(self.camera_orientation[0])
                dy = -math.sin(self.camera_orientation[0])
                dz = math.cos(self.camera_orientation[0]) * math.cos(self.camera_orientation[1])

                dummy_check_camera_x += dx
                dummy_check_camera_y += dy
                dummy_check_camera_z += dz

                dummy_check_camera = (dummy_check_camera_x, dummy_check_camera_y, dummy_check_camera_z)

                dummy_camera_distance = np.sqrt((point[0] - dummy_check_camera[0])**2 + (point[1] - dummy_check_camera[1])**2 + (point[2] - dummy_check_camera[2])**2)

                if current_camera_distance > dummy_camera_distance:
                    visible_points.append(point)
        return visible_points, visible_lines