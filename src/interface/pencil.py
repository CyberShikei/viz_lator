import pygame

# a pencil class that draws on the pygame screen


class Pencil:
    def __init__(self, screen, color, width):
        self.screen = screen
        self.color = color
        self.width = width

    def draw(self, start, end):
        color = self.color
        if start[1] == 0:
            color = (0, 0, 0)

        pygame.draw.line(self.screen, color, start, end, self.width)

    def draw_point(self, point, color=None):
        if not color:
            color = self.color
        
        pygame.draw.circle(self.screen, color, point, self.width)

    def draw_points(self, points):
        for point in points:
            # set color based on y value
            color = self.color
            # y = point[1]
            # if y < 0:
            #     y = point[1] * -1
            # while y > 255:
            #     y = point[1] - 255
            # color = (0, y, 0)
            self.draw_point((point[0], point[1]), color)

    def draw_lines(self, points, i=0):
        pnts = points
        if len(pnts) == 0:
            return 0
        if i == len(pnts) - 1:
            return 0
        self.draw(pnts[i], pnts[i + 1])
        return self.draw_lines(pnts, i + 1)

    def set_color(self, color):
        if not color:
            color = self.color
        if color[0] > 255 or color[1] > 255 or color[2] > 255:
            color = (255, 255, 255)
        if color[0] < 0:
            color = (color[0] * -1, 0, 0)
        if color[1] < 0:
            color = (0, color[1] * -1, 0)
        if color[2] < 0:
            color = (0, 0, color[2] * -1)
        self.color = color
