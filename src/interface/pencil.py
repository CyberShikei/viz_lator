import pygame

# a pencil class that draws on the pygame screen


class Pencil:
    def __init__(self, screen, color, width):
        self.screen = screen
        self.color = color
        self.width = width

    def draw(self, start, end):
        pygame.draw.line(self.screen, self.color, start, end, self.width)

    def draw_point(self, point, color=None):
        if not color:
            color = self.color
        pygame.draw.circle(self.screen, color, point, self.width)

    def draw_points(self, points):
        for point in points:
            self.draw_point(point)

    def draw_lines(self, points, i=0):
        pnts = points
        if len(pnts) == 0:
            return 0
        if i == len(pnts) - 1:
            return 0
        self.draw(pnts[i], pnts[i + 1])
        return self.draw_lines(pnts, i + 1)
