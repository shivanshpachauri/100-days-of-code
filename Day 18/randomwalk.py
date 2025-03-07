import turtle as t
from random import random
from random import choice
color=["red","blue","green","maroon","sandybrown","magenta","chocolate","purple"]
for i in range(100):
    t.color(choice(color))
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)