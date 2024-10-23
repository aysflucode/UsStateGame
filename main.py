import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states_name_list = data["state"].to_list()
guessed_list= []

while len(guessed_list) < 50:
    answer_state = screen.textinput( title= f"{len(guessed_list)}/50 States Correct", 
                                    prompt="What's another state").title()
    if answer_state == "Exit":
        missing_state = [state for state in states_name_list if state not in guessed_list]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break
    
    if answer_state in states_name_list:
        guessed_list.append(answer_state)
        write = turtle.Turtle()
        write.hideturtle()
        write.penup()
        state_data = data[data.state == answer_state]
        write.goto(int(state_data.x),int(state_data.y))
        write.write(answer_state)     









