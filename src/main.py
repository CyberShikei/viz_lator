#!../venv/bin/python3
import math
import pygame
import subprocess
import re
from interface import Window, Pencil
from graph import Graph

TITLE = "Viz Lator"
WIN_W = 1200
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

# function to replace . with , and convert to float


def convert_float(values: list):
    new_values = []
    for value in values:
        try:
            new_value = float(value)
            new_values.append(new_value)
        except ValueError:
            pass
    return new_values


def check_color(value):
    if value < 0:
        value = value * -1
    if value > 255:
        value = 255
    return value


def get_color(values):
    values[0] = (values[0] * 255) * 20
    values[1] = (values[1] % 255) * 4
    values[2] = (values[2] % 255) / 2
    color = (int)(check_color(values[0])), (int)(
        check_color(values[1])), (int)(check_color(values[2]))
    return color


def throttle_data_stream(new_data, last_data, rate_of_change: float = 0.5, max=20):
    if len(last_data) == 0:
        return new_data

    for i, item in enumerate(new_data):
        l_val = last_data[i]
        n_val = item

        change = n_val - l_val
        new_value = l_val + (change * rate_of_change)

        if new_value > max:
            new_value = max
        if new_value < 0:
            new_value = 0
        new_data[i] = new_value
        # print(f"last-item {last_data[i]} new-item {new_data[i]} change {change}")

    return new_data


def run(win):
    proc = subprocess.Popen(
        ["./audio_draw/target/debug/audio_draw"],
        stdout=subprocess.PIPE,
        text=True
    )

    tick = 0
    origin = win.get_center()
    w_min = origin[0]
    w_max = win.width
    g_width = (w_min, w_max)
    h_min = origin[1]
    h_max = win.height
    g_height = (h_min, h_max)

    last_data = []
    graph = Graph([], origin, g_width, g_height, 1)
    # graph = sine_graph(AMP, origin, g_width, TICK)
    # show_graph(graph)
    pencil = Pencil(win.screen, (255, 0, 0), 2)
    if proc.stdout is not None:
        for line in proc.stdout:
            # Clear screen
            win.clear_screen()
            # print(line)
            line = line.strip('"')
            data = line.split(":")
            meta_data = convert_float(data[1:])
            # new_color = get_color(meta_data[1:])
            # pencil.set_color(new_color)

            values = data[0].split(" ")  # Convert to integer
            # dominant_freq_index = (int)(meta_data[0])
            # dom_freq = (float)(values[dominant_freq_index])
            # print(f"dominant freq: {dom_freq}")

            dec_vals = convert_float(values)
            throttle = dec_vals #throttle_data_stream(dec_vals, last_data, 0.1, 7)
            last_data = dec_vals
            graph.set_graph(throttle)
            #print(graph.get_graph())
            pencil.draw_points(graph.graphic())
            graph.mirror_y()
            #pencil.draw_lines(graph.graphic())
            graph.mirror_x()
            pencil.draw_points(graph.graphic())
            graph.mirror_xy()
            #pencil.draw_lines(graph.graphic())

        # win.check_events()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        break
            pygame.display.flip()
            # win.clock.tick(win.fps)
    pygame.quit()
    exit(0)


def main():
    window = Window(WIN_W, WIN_H, TITLE)

    run(window)


if __name__ == "__main__":
    main()
