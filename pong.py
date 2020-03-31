import turtle
import winsound

wn=turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("orange")
wn.setup(width=600,height=600)
wn.tracer(0)

#Score
score_yellow = 0
score_green = 0


#board

board = turtle.Turtle()
board.shape("square")
board.color("white")
board.shapesize(stretch_wid=600,stretch_len=0.2)
board.goto(0,0)

#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250,0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(250,0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Yellow : 0   Green : 0",align="center",font=("Courier",24,"normal"))


#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y+=40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=40
    paddle_b.sety(y)

#Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"i")
wn.onkeypress(paddle_b_down,"k")



#Main Game loop
while True:
    wn.update()

    #Move the ball

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)

    if ball.xcor()>300:
        ball.goto(0,0)
        ball.dx *= -1
        score_yellow+=1
        pen.clear()
        pen.write(f"Yellow : {score_yellow}   Green : {score_green}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor()< -300:
        ball.goto(0,0)
        ball.dx *= -1
        score_green+=1
        pen.clear()
        pen.write(f"Yellow : {score_yellow}   Green : {score_green}", align="center", font=("Courier", 24, "normal"))

    #paddle and ball collision
    if ball.xcor() > 230 and (ball.ycor() > paddle_b.ycor()-40 and ball.ycor() < paddle_b.ycor()+40):
        ball.setx(230)
        ball.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)


    if ball.xcor() < -230 and (ball.ycor() > paddle_a.ycor()-40 and ball.ycor() < paddle_a.ycor()+40):
        ball.setx(-230)
        ball.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)

    #paddle boundaries

    if paddle_a.ycor() > 260:
        paddle_a.sety(260)

    if paddle_a.ycor() < -260:
        paddle_a.sety(-260)

    if paddle_b.ycor() > 260:
        paddle_b.sety(260)

    if paddle_b.ycor() < -260:
        paddle_b.sety(-260)








































