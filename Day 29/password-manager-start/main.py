from tkinter import *
from tkinter import messagebox
window=Tk()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email=email_entry.get()
    website=website_entry.get()
    password=password_entry.get()
    if(len(email)==0 or len(website)==0 or len(password)==0):
       messagebox.showinfo(title=f"{email}",message='Enter valid email or password')
    else:
        is_ok_cancel=messagebox.askokcancel(title=website,message=f'\nEmail :{email}\n Wesbite: {website}\n Password: {password}\n Is it ok to save?')
        if is_ok_cancel:
            combined=f"Email: {email}| Website : {website}| password {password}|\n"
            with open("data.txt",mode='+a') as file:
                file.write(combined)
            email_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

canvas=Canvas(width=200,height=200)


logo=PhotoImage(file="logo.png")


canvas.create_image(100,100,image=logo)


canvas.grid(row=0,column=1)
window.config(padx=50,pady=50)

website_label=Label(text='Website')
website_label.grid(row=1,column=0)

email_label=Label(text='Email')
email_label.grid(row=2,column=0)


password_label=Label(text='Password')
password_label.grid(row=3,column=0)

generate_password=Button(text="Generate password")
generate_password.grid(column=2,row=3)

Add_button=Button(text="Add",width=36,command=save)
Add_button.grid(column=1,row=4,columnspan=2)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)



email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)


password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


window.mainloop()