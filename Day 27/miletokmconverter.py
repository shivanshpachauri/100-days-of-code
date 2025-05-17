import tkinter
window=tkinter.Tk()
calculated=0
window.title("Mile to km generator")
window.minsize(width=500,height=300)

mylabel=tkinter.Label(text="Miles",font=("sans-serif",24))
mylabel.grid(column=2,row=0)

mylabel2=tkinter.Label(text=f'{calculated}',font=("sans-serif",24))
mylabel2.grid(column=1,row=1)



mylabel3=tkinter.Label(text="is equal to ",font=("sans-serif",24))
mylabel3.grid(column=0,row=1)


mylabel4=tkinter.Label(text="km",font=("sans-serif",24))
mylabel4.grid(column=2,row=1)

def button_clicked():

    inputvalue=float(input.get())
    calculated=inputvalue*1.60934
    print(calculated)
    mylabel2.config(text=f"{calculated}")




input=tkinter.Entry(width=10)
input.grid(column=1,row=0)





button=tkinter.Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)




window.mainloop()
