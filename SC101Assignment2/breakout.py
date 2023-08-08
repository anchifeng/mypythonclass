"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while 0 < lives <= 3:
        while True:
            if graphics.is_falling:
                graphics.ball_move()
            graphics.bounce()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.is_falling = False
                break
            pause(FRAME_RATE)
        graphics.reset_ball()
        if lives == 0:
            break
            

if __name__ == '__main__':
    main()
