import numpy as np
import keyboard

from settings import camera_settings
from math_formulas import move_camera

class camera():
    def __init__(self):
        self.camera_distance_from_detection_board = camera_settings.camera_distance_from_detection_board
        self.camera_pos = camera_settings.camera_default_position
        self.orientation_pitch = camera_settings.camera_default_orientation[0]
        self.orientation_roll = camera_settings.camera_default_orientation[1]
        self.orientation_yaw = camera_settings.camera_default_orientation[2]
        
    def camera_movement(self):

        if keyboard.is_pressed(camera_settings.forwards_key):
            self.camera_pos = move_camera((self.orientation_pitch, self.orientation_roll, self.orientation_yaw), self.camera_pos, 'forwards', camera_settings.camera_movement_speed)

        if keyboard.is_pressed(camera_settings.backwards_key):
            self.camera_pos = move_camera((self.orientation_pitch, self.orientation_roll, self.orientation_yaw), self.camera_pos, 'backwards', camera_settings.camera_movement_speed)

        if keyboard.is_pressed(camera_settings.right_key):
            self.camera_pos = move_camera((self.orientation_pitch, self.orientation_roll, self.orientation_yaw), self.camera_pos, 'right', camera_settings.camera_movement_speed)

        if keyboard.is_pressed(camera_settings.left_key):
            self.camera_pos = move_camera((self.orientation_pitch, self.orientation_roll, self.orientation_yaw), self.camera_pos, 'left', camera_settings.camera_movement_speed)
        

        if self.orientation_pitch > np.radians(-90):
            if keyboard.is_pressed(camera_settings.look_up_key):
                self.orientation_pitch -= camera_settings.camera_look_speed

        if self.orientation_pitch < np.radians(90):
            if keyboard.is_pressed(camera_settings.look_down_key):
                self.orientation_pitch += camera_settings.camera_look_speed

        if keyboard.is_pressed(camera_settings.look_right_key):
            self.orientation_roll += camera_settings.camera_look_speed
        if keyboard.is_pressed(camera_settings.look_left_key):
            self.orientation_roll -= camera_settings.camera_look_speed
        
        if self.orientation_roll >= np.radians(360):
            self.orientation_roll = 0
        if self.orientation_roll <= np.radians(-360):
            self.orientation_roll = 0
