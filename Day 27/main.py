import tkinter
window=tkinter.Tk()
window.title("first gui program")
window.minsize(width=500,height=300)
mylabel=tkinter.Label(text="I am a label",font=("serif",24,"bold"))
mylabel.pack()


input=tkinter.Entry(width=10)
input.pack()

def button_clicked():

    inputvalue=input.get()
    
    mylabel.config(text=f"{inputvalue}")

button=tkinter.Button(text="Click me",command=button_clicked)
button.pack()
window.mainloop()
