import turtle
import time
import random

SCREEN_SIZE = 600
FONT = ("Courier", 24, "normal")
SEGMENT_SIZE = 20
SEGMENT_COLOR = "grey"
FOOD_COLOR = "red"
MOVE_DELAY = 100

def create_screen():
    window = turtle.Screen()
    window.title("Snake Game")
    window.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    window.tracer(0)
    return window

def create_turtle(shape, color, penup=True):
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)
    turtle_obj.shape(shape)
    turtle_obj.color(color)
    if penup:
        turtle_obj.penup()
    return turtle_obj

def create_segment():
    return create_turtle("square", SEGMENT_COLOR)

def create_food():
    return create_turtle("circle", FOOD_COLOR)

def move():
    global last_move_direction
    if last_move_direction == "up":
        y = head.ycor()
        head.sety(y + SEGMENT_SIZE)

    elif last_move_direction == "down":
        y = head.ycor()
        head.sety(y - SEGMENT_SIZE)

    elif last_move_direction == "left":
        x = head.xcor()
        head.setx(x - SEGMENT_SIZE)

    elif last_move_direction == "right":
        x = head.xcor()
        head.setx(x + SEGMENT_SIZE)

def go_up():
    global last_move_direction
    if last_move_direction != "down":
        last_move_direction = "up"

def go_down():
    global last_move_direction
    if last_move_direction != "up":
        last_move_direction = "down"

def go_left():
    global last_move_direction
    if last_move_direction != "right":
        last_move_direction = "left"

def go_right():
    global last_move_direction
    if last_move_direction != "left":
        last_move_direction = "right"

def check_border_collision():
    global score, high_score, last_move_direction
    if head.xcor() > SCREEN_SIZE / 2 - SEGMENT_SIZE or head.xcor() < -SCREEN_SIZE / 2 + SEGMENT_SIZE or \
            head.ycor() > SCREEN_SIZE / 2 - SEGMENT_SIZE or head.ycor() < -SCREEN_SIZE / 2 + SEGMENT_SIZE:
        reset_game()
        last_move_direction = "stop"

def check_body_collision():
    global score, high_score, last_move_direction
    for segment in segments:
        if segment.distance(head) < SEGMENT_SIZE:
            reset_game()

def reset_game():
    global score, high_score, delay
    time.sleep(1)
    head.goto(0, 0)

    for segment in segments:
        segment.hideturtle()

    segments.clear()

    score = 0
    delay = 0.1

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=FONT)

def update_score():
    global score, high_score
    score += 10

    if score > high_score:
        high_score = score

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=FONT)

def check_food_collision():
    global delay
    if head.distance(food) < SEGMENT_SIZE:
        x = random.randint(-SCREEN_SIZE / 2 + SEGMENT_SIZE, SCREEN_SIZE / 2 - SEGMENT_SIZE)
        y = random.randint(-SCREEN_SIZE / 2 + SEGMENT_SIZE, SCREEN_SIZE / 2 - SEGMENT_SIZE)
        food.goto(x, y)

        new_segment = create_segment()
        segments.append(new_segment)

        update_score()

        delay -= 0.001

def update_segments():
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

def main():
    global head, segments, food, pen, last_move_direction, score, high_score, delay

    # Setup screen
    window = create_screen()

    # Setup Snake
    head = create_turtle("square", "black")
    head.goto(0, 0)
    head.direction = "stop"

    # Setup Snake Body
    segments = []

    # Score
    score = 0
    high_score = 0

    # Pen
    pen = create_turtle("square", "black")
    pen.hideturtle()
    pen.goto(0, SCREEN_SIZE / 2 - 30)
    pen.write("Score: 0  High Score: 0", align="center", font=FONT)

    # Setup Snake Food
    food = create_food()
    food.goto(0, 100)

    # Keybindings
    window.listen()
    window.onkeypress(go_up, "w")
    window.onkeypress(go_down, "s")
    window.onkeypress(go_left, "a")
    window.onkeypress(go_right, "d")

    last_move_direction = "stop"

    # Main game loop
    while True:
        window.update()

        check_border_collision()
        check_body_collision()
        check_food_collision()

        update_segments()
        move()

        time.sleep(MOVE_DELAY / 1000)

if __name__ == "__main__":
    main()
