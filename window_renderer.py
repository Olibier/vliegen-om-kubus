import pygame as pg
from settings import screen_settings
import sys

class window_renderer():
    def __init__(self):
        self.screen_width = screen_settings.screen_width
        self.screen_height = screen_settings.screen_height
        self.screen_title = screen_settings.screen_title
        self.screen_fps = screen_settings.screen_fps
        self.screen_background_color = screen_settings.screem_background_color

        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption(self.screen_title)

        self.screen.fill(self.screen_background_color)
        pg.display.flip()
    
    def check_exit(self):
        #Quit if user clicks cross
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def draw_dot(self, position, color, diameter):
        pg.draw.circle(self.screen, color, position, diameter/2)


        #Update screen
        pg.display.flip()
    
    def clear_screen(self):
        #Background updating
        self.screen.fill(self.screen_background_color)
