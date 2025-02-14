
from .pencil import Pencil

MIN = 0
MAX = 360

AMP = 1


def play(pencil: Pencil, tick, graph=[], amp=AMP, bounds=(MIN, MAX)):

    # graph = adjust(graph, tick, amp, bounds)
    # new_graph = shift(graph, bounds)
    # pencil.draw_points(graph)
    pencil.draw_lines(graph)
    # return new_graph
    # pencil.draw_point(graph[0], color=(0, 255, 0))


def adjust(graph, tick, amp, bounds):
    new_graph = []
    for cord in graph:
        new_cord = (cord[0] + (tick * amp), cord[1])
        if new_cord[0] > bounds[1]:
            new_cord = (bounds[0] + (new_cord[0] - bounds[1]), new_cord[1])
        if new_cord[0] < bounds[0]:
            new_cord = (bounds[1] + (new_cord[0] - bounds[0]), new_cord[1])
        new_graph.append(new_cord)
        # print(cord)
    return new_graph


def shift(graph, bounds):
    new_graph = []
    back = graph[bounds[1]:]
    front = graph[bounds[0]:bounds[1] - 1]
    new_graph = back + front
    return new_graph
