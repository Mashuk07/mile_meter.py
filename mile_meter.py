from tkinter import *

window = Tk()
window.minsize(150,150)
window.config(padx=60,pady=50)
window.title("Mile to KM")

#label

is_equal_to = Label(text="Is equal to",)
is_equal_to.grid(row=2, column=1)

miles = Label(text="Miles")
miles.grid(row=1,column=4)

kilometer_entry = Label(text="Km")
kilometer_entry.grid(row=2,column=4)

output = Label(text="0")
output.grid(row=2,column=3)

#Buttons
def converter():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    output.config(text=km)
    return km
button = Button(text="Calculate",command=converter)
button.grid(row=3,column=3)
button.config()

#Entry
miles_entry = Entry(width=7)
miles_entry.grid(row=1,column=3)










window.mainloop()