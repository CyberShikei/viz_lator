import math
import pygame
from interface import Window, Pencil, play

TITLE = "Viz Lator"
WIN_W = 800
WIN_H = 600

DIV = 1
SPEED = 1
TICK = 5
AMP = 100


def turn_deg(num, inc=1):
    while num % 360 != 0:
        num += inc
    return num


def check_tick(tick, inc=1):
    up = True
    if tick > 360/DIV:
        up = False
    if tick < -360/DIV:
        up = True
    if up:
        tick += inc
    else:
        tick = -360/DIV

    return tick


def toggle(bool_in):
    return not bool_in


def sine_graph(amp, origin=(0, 0), rang=(0, 360), inc=1) -> list:
    graph = []
    count = 0
    while count < rang[1]:
        x = (int)(count + origin[0])
        angle = math.radians(count)
        y = (int)((math.sin(angle) * amp) + origin[1])
        graph.append((x, y))
        count += inc
    return graph


def replace(cord1, cord2):
    x_c1 = cord1[0]
    x_c2 = cord2[0]
    t_c1 = (x_c2, cord1[1])
    t_c2 = (x_c1, cord2[1])
    return t_c1, t_c2


def shift(graph, pos=0):
    if len(graph) == 0:
        return graph
    if pos == len(graph) - 1:
        return graph
    if pos == 0:
        o_y = graph[0][1]
        new_cord = (graph[-1][0], o_y)
        graph[-1] = new_cord

    # new_graph = []
    # for i in range(len(graph) - 1):
    n_y = graph[pos + 1][1]
    new_cord = (graph[pos][0], n_y)
    graph[pos] = new_cord

    return shift(graph, pos + 1)

def shift_r(graph, amnt=1):
    if amnt == 0:
        return graph
    result = shift(graph)
    return shift_r(result, amnt - 1)

def show_graph(graph):
    cols = 5
    count = 1
    text = ""
    for cord in graph:
        if count % cols == 0:
            print(text)
            text = ""
        else:
            text += f"{cord},\t"
        count += 1
    print(len(graph))


def run(win):
    tick = 0
    origin = (0, win.get_center()[1])
    g_min = 0
    g_max = win.width
    g_width = (g_min, turn_deg(g_max * SPEED, TICK))
    graph = sine_graph(AMP, origin, g_width, TICK)
    # show_graph(graph)
    pencil = Pencil(win.screen, (255, 0, 0), 2)
    while win.running:
        # Clear screen
        win.clear_screen()

        # if draw_toggle:
        # new_graph = play(pencil, tick, graph, SPEED, (g_min, g_max))
        # graph = new_graph
        play(pencil, tick, graph, SPEED, (g_min, g_max))

        # origin = (origin[0] + tick, origin[1])
        # new_graph = sine_graph(AMP, origin, g_width, TICK)
        new_graph = shift_r(graph, SPEED)
        #print(tick/TICK)
        #show_graph(new_graph[:TICK])
        graph = new_graph

        tick = check_tick(tick, TICK)

        # win.check_events()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    win.running = False
        pygame.display.flip()
        win.clock.tick(win.fps)
    pygame.quit()
    exit(0)


def main():
    window = Window(WIN_W, WIN_H, TITLE)

    run(window)


if __name__ == "__main__":
    main()
