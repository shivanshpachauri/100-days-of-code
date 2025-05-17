import tkinter
window=tkinter.Tk()
window.title("first gui program")
window.minsize(width=500,height=300)

mylabel=tkinter.Label(text="label",font=("serif",24,"bold"))
mylabel.grid(column=0,row=0)


button=tkinter.Button(text="additional button")
button.grid(column=2,row=0)

input=tkinter.Entry(width=10)
input.grid(column=3,row=2)

def button_clicked():

    inputvalue=input.get()
    
    mylabel.config(text=f"{inputvalue}")

button=tkinter.Button(text="Click me",command=button_clicked)
button.grid(row=1,column=1)



window.mainloop()
