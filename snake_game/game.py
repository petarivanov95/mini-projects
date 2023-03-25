import turtle
import time
import random
from tkinter import *

delay = 0.1
SCREEN_SIZE = 600
FONT = ("Courier", 24, "normal")
SEGMENT_SIZE = 20
SEGMENT_COLOR = "green"
HEAD_COLOR = "black"
FOOD_COLOR = "red"
MOVE_DELAY = 100

# Setup screen
window = turtle.Screen()
window.title("Snake Game")
window.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
window.tracer(0)  # turns off screen updates

# Setup Snake HEAD
head = turtle.Turtle()
head.speed(0)  # animation speed 0 is fastest
head.shape("square")
head.color(HEAD_COLOR)
head.penup()  # prevents the typical turtle line drawing
head.goto(0, 0)  # sets the turtle at the origin
head.direction = "stop"

# Setup Snake Body:
segments = []  # list is empty by default as there is only head when the game starts

# Score
score = 0
high_score = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=FONT)

# Setup Snake Food
food = turtle.Turtle()
food.speed(0)  # animation speed 0 is fastest
food.shape("circle")
food.color(FOOD_COLOR)
food.penup()  # prevents the typical turtle line drawing
food.goto(0, 100)  # sets the turtle at the origin


# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + SEGMENT_SIZE)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - SEGMENT_SIZE)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - SEGMENT_SIZE)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + SEGMENT_SIZE)


# The checks make sure that the snake can't move in the opposite direction
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def create_segment(color):
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color(color)
    new_segment.penup()
    return new_segment


# Keybindings

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# main game loop
while True:
    window.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            # segment.goto(1000,1000)
            segment.hideturtle()

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1
        #
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=FONT)

    if head.distance(food) < SEGMENT_SIZE:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = create_segment(SEGMENT_COLOR)
        segments.append(new_segment)

        # Update the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=FONT)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < SEGMENT_SIZE:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.hideturtle()

            # Clear the segments list
            segments.clear()

    time.sleep(delay)

window.mainloop()
