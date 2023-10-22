import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
pencil = turtle.Turtle()
pencil.hideturtle()
pencil.penup()
turtle.shape(image)

# get data from csv file
fifty_states_data = pandas.read_csv("50_states.csv")
fifty_state_list = fifty_states_data["state"].to_list()
print(fifty_state_list)
guessed_states = []

while len(guessed_states) < 50:
    # Get user's answer
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in fifty_state_list:
            if state not in guessed_states:
                states_to_learn.append(state)
        states_to_learn_dict = {
            "States to Learn": states_to_learn
        }
        new_data = pandas.DataFrame(states_to_learn_dict)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in fifty_state_list:
        guessed_states.append(answer_state)
        state = fifty_states_data[fifty_states_data.state == answer_state]
        pencil.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
        pencil.write(answer_state.title())

screen.exitonclick()
# The code below is how we got the x and y values of all states in the csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
