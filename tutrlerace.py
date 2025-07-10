
import turtle
import time
import random
import sys


WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "orange",
          "purple", "pink", "brown", "cyan", "magenta"]


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)

            if 2 <= racers <= 10:
                return racers
            else:
                print(
                    "Invalid number of racers. Please enter a number between 2 and 10.")

        else:
            print("Invalid input. Try Again!")


def race(colors):
    turtles = create_tutrle(colors)
    finish_line = HEIGHT // 2 - 10  # 10 px margin from the top
    while True:
        for i, racer in enumerate(turtles):
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= finish_line:
                # Pause to show the winner, then return the color
                time.sleep(1)
                return colors[i]


def create_tutrle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_tutrle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing! ")


racers = get_number_of_racers()
init_tutrle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner is {winner}!")
input("Press Enter to close the window...")
print(f"The winner is {winner}!")
turtle.bye()
