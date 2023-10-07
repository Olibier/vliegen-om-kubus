import pygame as pg
import sys

class renderer():
    def __init__(self, screen_width, screen_height, background_color, screen_fps, render_color, point_size, line_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = background_color
        self.screen_fps = screen_fps
        self.render_color = render_color
        self.point_size = point_size
        self.line_size = line_size

        self.screen = pg.display.set_mode((self.screen_height, self.screen_width))
        self.clock = pg.time.Clock()
    
    def update_screen(self, points_to_renderXY, lines_to_renderXY):
        self.screen.fill(self.background_color)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        for point in points_to_renderXY:
            pg.draw.circle(self.screen, self.render_color, (point[0], point[1]), self.point_size)
        
        for line in lines_to_renderXY:
            pg.draw.line(self.screen, self.render_color, line[0], line[1], self.line_size)

        self.clock.tick(self.screen_fps)
        pg.display.set_caption(str(self.clock.get_fps()))
        pg.display.flip()

