class screen_settings():
    screen_width = 500
    screen_height = 500
    screen_title = '3d Renderer by Olivier'
    screen_fps = 144
    screem_background_color = (255, 255, 255)
    x_max = 5
    y_max = 5

class camera_settings():
    camera_distance_from_detection_board = 20
    camera_default_position = (0, 0, -10)
    camera_default_orientation = (0, 0, 0)

    camera_movement_speed = 0.1
    camera_look_speed = 0.01

    display_surface_position = (0, 0, 10)

    forwards_key = 'w'
    backwards_key = 's'
    right_key = 'd'
    left_key = 'a'

    look_right_key = 'right arrow'
    look_left_key = 'left arrow'
    look_up_key = 'up arrow'
    look_down_key = 'down arrow'

class colors():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0,0,255)
    RED = (255, 0, 0)
