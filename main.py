from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=500)

score = 0
loses = 0
while loses < 3:
    turtles = []
    colors = ["red", "yellow", "green", "purple", "cyan", "orange"]
    for i in range(6):
        tim = Turtle()
        tim.penup()
        tim.shape("turtle")
        tim.color(colors[i])
        tim.goto(-230, (i - 3) * 50 + 20)
        turtles.append(tim)
    race_is_on = False
    bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
    if bet:
        race_is_on = True
    while race_is_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                race_is_on = False
                if bet == turtle.pencolor():
                    score += 1
                    print(f"You've won! {turtle.pencolor()} is the winning turtle.")
                else:
                    loses += 1
                    print(f"You've lost! {turtle.pencolor()} is the winning turtle.")
                break
            rand_dist = random.randint(0, 7)
            turtle.forward(rand_dist)
    my_screen.clear()
print("Your final score is ", score)
my_screen.exitonclick()  # © MTIRI WISSEM
