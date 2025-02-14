import pygame
import math


class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.running = True

        self.fps = 60
        pygame.init()

    def clear_screen(self):
        # Clear screen
        self.screen.fill((0, 0, 0))

    def check_events(self):
        for event in pygame.event.get():
            # on key press `q`
            if ((event.type == pygame.QUIT)
                    or (event.type == pygame.KEYDOWN
                        and event.key == pygame.K_q)):
                self.running = False
                pygame.quit()

            pygame.display.flip()
            self.clock.tick(self.fps)

    def get_center(self):
        return (self.width // 2, self.height // 2)


def turn_deg(num):
    while num % 360 != 0:
        num += 1
    return num


def check_tick(tick):
    up = True
    if tick > 360/DIV:
        up = False
    if tick < -360/DIV:
        up = True
    if up:
        tick += 1
    else:
        tick = -360/DIV

    return tick


def toggle(bool_in):
    return not bool_in


def sine_graph(amp, origin=(0, 0), rang=(0, 360)) -> list:
    graph = []
    for i in range(*rang):
        x = (int)(i + origin[0])
        angle = math.radians(i)
        y = (int)((math.sin(angle) * amp) + origin[1])
        graph.append((x, y))
    return graph

# if __name__ == "__main__":
#     window = Window(800, 600, "Viz Lator")
#     window.run()
