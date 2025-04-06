from turtle import Screen ,Turtle
import pandas as pd
timmy=Turtle()
screen=Screen()
img='blank_states_img.gif'
screen.addshape(img)
timmy.shape(img)
df=pd.read_csv("50_states.csv")
count=0
final_state={}
for i in range(0,50):
    timmy2=Turtle()
    answer_state=screen.textinput(title=f"quiz : {count}/50",prompt="Enter the state name")
    title_case=answer_state.title()
    timmy2.penup()
    if title_case=="Exit":
        finaldf=pd.DataFrame(final_state)
        finaldf.to_csv("high_score.csv")
        break
    correct_state=df[df['state']==title_case]
    if correct_state.empty!=True:
        count=count+1
        x_cor=correct_state.x
        y_cor=correct_state.y
        final_state.update(correct_state)
        timmy2.goto(x_cor.values[0],y_cor.values[0])
        timmy2.write(title_case)

print(final_state)
screen.exitonclick()