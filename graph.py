import os
import math

CLEAR_SCREEN = "\033[2J"
MOVE_CURSOR = "\033[{};{}H"

def draw_graph():
    print(CLEAR_SCREEN)
    
    width, height = os.get_terminal_size()
    x_scale = 1  # each step in x is x_scale columns wide
    y_scale = 1  # each step in y is y_scale row tall

    for x in range(0, width, x_scale):
        print(MOVE_CURSOR.format(height-1, x) + "-")  # x-axis

    for y in range(height):
        print(MOVE_CURSOR.format(height-1-y, 0) + "|")  # y-axis
    
    for x in range(width // x_scale):
        y = 3 * x 
        y_pos = height - 1 - y // y_scale
        x_pos = x * x_scale

        if 0 <= y_pos < height and 0 <= x_pos < width:
            print(MOVE_CURSOR.format(y_pos, x_pos) + "/")  # plot the point

    # move the cursor below the graph after drawing
    print(MOVE_CURSOR.format(height, 0))
    
draw_graph()