"""
File: draw_line.py
Name: Feng Angie
-------------------------
There is a circle indicating the user’s first click on window.
A line appears at the condition where the circle disappears
as the user clicks on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow(width=800, height=400)
hole = GOval(SIZE * 2, SIZE * 2)
n = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_hole)


def create_hole(mouse):
    global n
    if n % 2 != 0:
        window.add(hole, x=mouse.x - hole.width / 2, y=mouse.y - hole.height / 2)
        n += 1
    else:  # n % 2 == 0:
        line = GLine(hole.x + hole.width / 2, hole.y + hole.height / 2, mouse.x, mouse.y)
        window.remove(hole)
        window.add(line)
        n += 1


if __name__ == "__main__":
    main()
