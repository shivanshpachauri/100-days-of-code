from turtle import Screen,Turtle
import pandas as pd
screen=Screen()
timmy=Turtle()
# longitudes = y-co-ordinates
# latitude=x-co-ordinates
img='india_map.gif'
screen.addshape(img)
df=pd.read_csv("India States-UTs.csv")

answer_state=screen.textinput(title="states quiz",prompt="Enter the state name")
title_case=answer_state.title()
x=df[df['State/UT']==title_case].Latitude
y=df[df['State/UT']==title_case].Longitude
print(title_case,"\n")
print("\nLatitude : ",x,"\nLongitude : ",y)
# screen.write("\nLatitude : ",x,"\nLongitude : ",y)
timmy.shape(img)
screen.exitonclick()