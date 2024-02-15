import turtle as t
import pandas as pd

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

name_writer = t.Turtle()
name_writer.penup()
name_writer.hideturtle()

states = pd.read_csv("50_states.csv")

remaining_states = states.state.to_list()
states_guessed = 0
correct_guesses = []
game_on = True
while game_on:
    guess = screen.textinput(f"{states_guessed}/50 States Correct", "What's a state name?"  if states_guessed == 0 else "What's another state name?").title()

    if guess == "Exit":
        break

    if guess.title() in remaining_states:
        row = states[states.state == guess]
        state = row.state.item()
        state_x = int(row.x.item())
        state_y = int(row.y.item())

        name_writer.goto(state_x, state_y)
        name_writer.write(state, align=ALIGNMENT, font=FONT)
        correct_guesses.append(row.state.item())
        states_guessed += 1
        remaining_states.remove(guess.title())

    if states_guessed == 50:
        game_on = False

states[~states.state.isin(correct_guesses)].state.to_csv("states_to_learn.csv")