from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min=math.floor(count/60)
    count_sec=count%60
    if(len(str(count_sec))==1):
        count_sec=f"0{count_sec}"

    if(len(str(count_min))==1):
        count_min=f"0{count_min}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)
    else:
        timer_start()
        print(reps)
        

def timer_start():
    global reps
    reps+=1
    work_sec=WORK_MIN*60 #25
    short_break_sec=SHORT_BREAK_MIN*60 #5
    long_break_sec=LONG_BREAK_MIN*60 #20

    if reps==8:
        count_down(long_break_sec)
        label.config(text="do 20 min work")
    elif reps%2==0 and reps!=0:
        count_down(short_break_sec)

        label.config(text="take a short  break 5 min")
    else:
        count_down(work_sec)

        label.config(text="take a long break 25 min")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=100,pady=50,bg=YELLOW)

label=Label(text="Timer",bg=YELLOW,fg=GREEN,font=("Sans-serif",24,"bold"))
label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)

timer_text=canvas.create_text(100,138,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

    
button_start=Button(text="Start",bg=YELLOW,command=timer_start)


button_reset=Button(text="Reset",bg=YELLOW)


button_check=Label(text="✔",fg=GREEN,bg=YELLOW)

button_start.grid(column=0,row=2)
button_reset.grid(column=2,row=2)
button_check.grid(column=1,row=3)
window.mainloop()
