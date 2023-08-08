"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # 請把所有 attributes都寫成 private(重點整理）
        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self.window.add(self._paddle, x=(self.window.width-self._paddle.width)/2,
                        y=self.window.height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2,
                        y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        self.is_falling = False

        # Initialize our mouse listeners
        onmouseclicked(self.drop_ball)
        onmousemoved(self.following_paddle)

        # Draw bricks
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = (brick_width + brick_spacing) * col
                y = brick_offset + (brick_height + brick_spacing) * row
                self._brick = GRect(brick_width, brick_height, x=x, y=y)
                self._brick.filled = True
                if 0 <= row < 2:
                    self._brick.fill_color = "red"
                elif 2 <= row < 4:
                    self._brick.fill_color = 'orange'
                elif 4 <= row < 6:
                    self._brick.fill_color = 'yellow'
                elif 6 <= row < 8:
                    self._brick.fill_color = 'green'
                elif 8 <= row < brick_rows:
                    self._brick.fill_color = 'blue'
                self.window.add(self._brick)

        # Extensions
        self.score = 0
        self.score_label = GLabel("Score: " + str(self.score))
        self.window.add(self.score_label, x=0, y=self.score_label.height)

    def following_paddle(self, event):
        self._paddle.x = event.x - self._paddle.width / 2
        if self._paddle.x >= self.window.width - self._paddle.width:
            self._paddle.x = self.window.width - self._paddle.width
        elif self._paddle.x <= 0:
            self._paddle.x = 0
        # self._paddle.y = self.window.height-paddle_offset-self._paddle.height

    def drop_ball(self, event):
        self.is_falling = True
        if self.__dx == 0 and self.__dy == 0:
            self.ball_move()

    def ball_move(self):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(0, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
        else:
            self.ball.move(self.__dx, self.__dy)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_ball(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def bounce(self):
        # window left and right side
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        # window upper side
        elif self.ball.y <= 0:
            self.__dy = -self.__dy
        # paddle
        if self._paddle.y <= self.ball.y + self.ball.height <= self._paddle.y + self._paddle.height:
            if self._paddle.x <= self.ball.x + self.ball.width <= self._paddle.x + self._paddle.width:
                self.__dy = -self.__dy
        # bricks
        ball_a = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_b = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        ball_c = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        ball_d = self.window.get_object_at(self.ball.x+ self.ball.width, self.ball.y + self.ball.height)
        if ball_a is not None and ball_a is not self.score_label and ball_a is not self._paddle:
            _ = self.window.get_object_at(self.ball.x-1, self.ball.y-1)
            self.window.remove(_)
            self.score += 1
            self.__dy = -self.__dy
            self.score_label.text = 'Score: ' + str(self.score)
        if ball_b is not None and ball_b is not self.score_label and ball_b is not self._paddle:
            _ = self.window.get_object_at(self.ball.x + self.ball.width+1, self.ball.y-1)
            self.window.remove(_)
            self.score += 1
            self.__dy = -self.__dy
            self.score_label.text = 'Score: ' + str(self.score)
        if ball_c is not None and ball_c is not self.score_label and ball_c is not self._paddle:
            _ = self.window.get_object_at(self.ball.x-1, self.ball.y + self.ball.height+1)
            self.window.remove(_)
            self.score += 1
            self.__dy = -self.__dy
            self.score_label.text = 'Score: ' + str(self.score)
        if ball_d is not None and ball_d is not self.score_label and ball_d is not self._paddle:
            _ = self.window.get_object_at(self.ball.x + self.ball.width+1, self.ball.y + self.ball.height+1)
            self.window.remove(_)
            self.score += 1
            self.__dy = -self.__dy
            self.score_label.text = 'Score: ' + str(self.score)
