import turtle

# Set up game screen
win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turns off automatic screen updates

# Create paddles
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# Create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Adjust ball speed
ball.dy = 0.15  # Adjust ball speed

# Create score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Game rules
game_over = False
winner = None
points = {"player1": 0, "player2": 0}
game_rules = {"max_points": 5}  # Update max points to 5

# Function to move paddles
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    if y > 250:  # Limit paddle movement
        y = 250
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    if y < -240:  # Limit paddle movement
        y = -240
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    if y > 250:  # Limit paddle movement
        y = 250
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    if y < -240:  # Limit paddle movement
        y = -240
    paddle2.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")

# Main game loop
while not game_over:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Check for ball going off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player1"] += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player2"] += 1

    # Check for ball colliding with top or bottom of screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Update score display
    score_display.clear()
    score_display.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))

    # Check for game over
    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = "player1"
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = "player2"

# Display winner
if winner:
    score_display.clear()
    score_display.write("Game Over! Winner: {}".format(winner), align="center", font=("Arial", 24, "normal"))

win.mainloop()
