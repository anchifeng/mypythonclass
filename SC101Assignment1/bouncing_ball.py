"""
File: bouncing_ball.py
Name: Feng Angie
-------------------------
This process of simulating the ball falling is controlled by mouse click.
And it can be click three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

ball = GOval(SIZE, SIZE)
window = GWindow(800, 500, title='bouncing_ball.py')
count = 0
is_falling = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(drop_ball)


def drop_ball(mouse):
    global is_falling
    global count
    if not is_falling and count < 3:
        is_falling = True
        vy = 0
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            pause(DELAY)
            if ball.y+SIZE >= window.height:
                vy = -vy * REDUCE
            if ball.x+SIZE > window.width:
                break
        window.remove(ball)
        is_falling = False
        window.add(ball, x=START_X, y=START_Y)
        count += 1


if __name__ == "__main__":
    main()
