import turtle


class Pong:
    def __init__(self):
        self.make_window()
        self.paddleA = self.make_paddle()
        self.paddleA.goto(-350, 0)
        self.paddleB = self.make_paddle()
        self.paddleB.goto(350, 0)
        self.paddle_speed = 25
        self.make_ball()
        self.make_pen()

    def make_window(self):
        window = turtle.Screen()
        window.title('Pong')
        window.bgcolor('black')
        window.setup(width=800, height=600)
        window.tracer(0)
        self.window = window

    def make_paddle(self):
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape('square')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.color('white')
        paddle.penup()
        paddle.score = 0
        return paddle

    def make_ball(self):
        ball = turtle.Turtle()
        ball.shape('square')
        ball.color('white')
        ball.speed(0)
        ball.penup()
        ball.dx = 1
        ball.dy = -1
        self.ball = ball
        
    def make_pen(self):
        pen = turtle.Turtle()
        #pen.speed(0)
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        self.pen = pen

    def write_scores(self):
        pen = self.pen
        pen.goto(0, 260)
        scores = 'Player A: {}   Player B: {}'.format(
            self.paddleA.score, self.paddleB.score
        )
        pen.clear()
        pen.write(scores, align='center', font=('Courier', 20))

    def ghosts(self, players):
        from random import choice
        paddles = [self.paddleA]
        if players == '0':
            paddles.append(self.paddleB)
        for paddle in paddles:
            direction = choice([-1, 1])
            paddle.sety(
                paddle.ycor() + self.paddle_speed * direction)
            if paddle.ycor() > 290:
                paddle.sety(290)
            if paddle.ycor() < -290:
                paddle.sety(-290)

    def balling(self):
        ball = self.ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            self.paddleA.score += 1
            ball.goto(0, 0)
            ball.dx *= -1
            self.write_scores()

        if ball.xcor() < -390:
            self.paddleB.score +=1
            ball.goto(0, 0)
            ball.dx *= -1
            self.write_scores()

        if (
            340 < ball.xcor() < 350 and
            ball.ycor() < self.paddleB.ycor() + 60 and
            ball.ycor() > self.paddleB.ycor() - 60
            ):
                ball.setx(340)
                ball.dx *= -1

        if (
            -340 > ball.xcor() > -350 and
            ball.ycor() < self.paddleA.ycor() + 60 and
            ball.ycor() > self.paddleA.ycor() - 60
            ):
                ball.setx(-340)
                ball.dx *= -1

    def Aup(self):
        self.paddleA.sety(self.paddleA.ycor() + self.paddle_speed)

    def Bup(self):
        self.paddleB.sety(self.paddleB.ycor() + self.paddle_speed)

    def Adown(self):
        self.paddleA.sety(self.paddleA.ycor() - self.paddle_speed)

    def Bdown(self):
        self.paddleB.sety(self.paddleB.ycor() - self.paddle_speed)

    def go(self, players):
        if players != '0':
            self.window.listen()
            self.window.onkeypress(self.Bup, 'i')
            self.window.onkeypress(self.Bdown, 'k')
            if players == '2':
                self.window.onkeypress(self.Aup, 'w')
                self.window.onkeypress(self.Adown, 's')
           


if __name__ == '__main__':
    print('no')