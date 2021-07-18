#Simple Pong game in Python 3.9.5. lets try it out lmaoo
# gay looking boy what you say looking boy?
import turtle

initial_speed = 0.4

win = turtle.Screen()
win.title("Pong by killkennyale")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation of paddle
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.color("white")
paddle_a.penup() #turtle draws lines, we don't want that duh
paddle_a.goto(-350,0) #coordinates for turtle-paddle


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation of paddle
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.color("white")
paddle_b.penup() #turtle draws lines, we don't want that duh
paddle_b.goto(350,0) #coordinates for turtle-paddle


# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation of ball
ball.shape("square")
# ball.shapesize(stretch_wid=1, stretch_len=1) 
ball.color("white")
ball.penup() #turtle draws lines, we don't want that duh
ball.goto(0,0) #coordinates for turtle-ball
ball.dx = initial_speed #speed of x
ball.dy = initial_speed #speed of y

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # we don't need to see it
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

# now we gotta make the paddle move using a keyboard

# Function
def paddle_a_up():
    y = paddle_a.ycor() #assign y-coordinate to variable y
    y = y + 20 #add 20 pixels to y-coordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #assign y-coordinate to variable y
    y = y - 20 #add 20 pixels to y-coordinate
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #assign y-coordinate to variable y
    y = y + 20 #add 20 pixels to y-coordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #assign y-coordinate to variable y
    y = y - 20 #add 20 pixels to y-coordinate
    paddle_b.sety(y)

# Keyboard Binding
win.listen() # tells the turtle to listen to the keyboard
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
# when we press 'w'or's' then it calls paddle_a_up or down and adds or subtracts 20 to the y coordinate
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
# when we press 'up'or'down' arrow then it calls paddle_b_up or down and adds or subtracts 20 to the y coordinate


#Main Game Loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290) # it reaches roof at 300
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290) # it reaches roof at 300
        ball.dy *= -1
   
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = initial_speed
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = initial_speed
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        