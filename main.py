from tkinter import *

window = Tk()
window.title("My first gui program")
window.minsize(500,300)
window.config(padx=10,pady=10)
mylabel = Label(text = "Hello world", font=("Arial",25,"bold"))
mylabel.grid(row=0,column=0)

#Button

def button_clicked():
    pass

button = Button(text="Click me",command=button_clicked)
button.grid(row=1,column=1)

new_button = Button(text="New Button")
new_button.grid(row=0,column=3)

#Entry

input = Entry(width=35)
input.grid(row=7,column=4)
print(input.get())



window.mainloop()