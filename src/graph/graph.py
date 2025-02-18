from typing import List, Tuple
from itertools import islice
import numpy as np


class Graph:
    def __init__(self, graph: List[float] = [], resolution=1):
        self._resolution = resolution
        self._graph: List[float] = graph

    def _disolve_resolution(self) -> List[float]:
        if len(self._graph) == 0:
            return []
        average_list = _chunk_averages(self._graph, self._resolution)
        print(average_list)
        return average_list

    def get_graph(self) -> List[float]:
        #return self._average_graph()
        return self._graph

    def _average_graph(self):
        return self._disolve_resolution()

    def __append__(self, item):
        self._graph.append(item)

    def __str__(self):
        return str(self._graph)

    def __repr__(self):
        return str(self._graph)

    def __len__(self):
        return len(self._graph)

    def __getitem__(self, index):
        return self._graph[index]

    def __setitem__(self, index, value):
        self._graph[index] = value

    def __iter__(self):
        return iter(self._graph)

    def __enumerate__(self):
        return enumerate(self._graph)

    def __contains__(self, item):
        return item in self._graph

    def __reversed__(self):
        return reversed(self._graph)


def _chunks(lst, n):
    n = len(lst) // n
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def _chunkify(lst, n):
    """Splits a list into n chunks."""
    it = iter(lst)
    n_lst = [list(islice(it, i)) for i in [len(lst) // n +
                                           (1 if x < len(lst) % n else 0) for x in range(n)]]
    print(n_lst)
    return n_lst


def _split_into_chunks(lst, n):
    """Splits a list into n approximately equal chunks."""
    k, m = divmod(len(lst), n)
    n_lst = [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)]
             for i in range(n)]
    print(n_lst)
    return n_lst


def _chunk_averages(lst, n):
    """Splits list into n chunks and returns their averages."""
    chunks = _chunks(lst, n)
    for chunk in chunks:
        print(f"{chunk}\n\n")
    # Avoid division by zero
    avrgs = [sum(chunk) / len(chunk) for chunk in chunks if chunk]
    print(avrgs)
    return avrgs




class GraphicGraph(Graph):
    _cords: List[Tuple[int, int]]
    _origin: Tuple[int, int]
    _x_r: Tuple[int, int]
    _y_r: Tuple[int, int]

    def __init__(self,
                 decimal_values: List[float],
                 origin=(0, 0),
                 x_range=(0, 360),
                 y_range=(0, 100),
                 resolution=1
                 ):
        super().__init__(decimal_values, resolution)
        self._cords: List[Tuple[int, int]] = []
        self._origin = origin
        self._x_r = x_range
        self._y_r = y_range

        self._init_cords()

    def cords(self):
        return self._cords

    def origin(self):
        return self._origin

    def d_x(self):
        len_x = len(self.get_graph())
        if len_x == 0:
            len_x = 1
        dx = (self._x_r[1] - self._x_r[0]) / len_x
        return dx

    def d_y(self):
        try:
            max_y = max(self.get_graph())
        except ValueError:
            max_y = 0
        if max_y == 0:
            max_y = 1
        dy = (self._y_r[1] - self._y_r[0]) / max_y
        return dy

    def reset(self):
        self._init_cords()

    def copy(self):
        return GraphicGraph(self.get_graph(), self._origin, self._x_r, self._y_r)

    def mirror_y(self):
        self._init_cords((False, True))

    def mirror_x(self):
        self._init_cords((True, False))

    def mirror_xy(self):
        self._init_cords((True, True))

    def set_graph(self, decimal_values: List[float]):
        super().__init__(decimal_values)
        self._init_cords()

    def graphic(self) -> List[Tuple[int, int]]:
        return self._cords

    def _set_cord(self, cord: Tuple[int, int]):
        self._cords.append(cord)

    def _init_cords(self, mirror=(False, False)):
        self._cords = []
        for index, value in super().__enumerate__():
            if mirror[0]:
                x = self._origin[0] - (int)(index * self.d_x())
            else:
                x = (int)(index * self.d_x()) + self._origin[0]
            if mirror[1]:
                y = self._origin[1] - (int)(value * self.d_y())
            else:
                y = (int)(value * self.d_y()) + self._origin[1]
            self._set_cord((x, y))
