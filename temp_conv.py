from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Temperature-Converter")
root.configure(bg= "white")
root.geometry("550x200")

temp_label = Label(root,text="TEMPERATURE CONVERTER",font=("Helvetica", 15), fg="#720a33",bg="white")
temp_label.grid(row=0, column=2,pady=5)


# TYPES
From_type = Label(root,text="From",font=("Oswald",15),bg="white",fg="#720a33")
From_type.grid(row=1, column=0)
To_type = Label(root,text="To",font=("Oswald",15),bg="white",fg="#720a33")
To_type.grid(row=3, column=0)

# conversion
def show():
    from_type = clicked.get()
    to_type = pressed.get()
    if from_type == "Fahrenheit" and to_type == "Celsius":
        value = ema.get()
        F_C = 5 / 9 * (float(value) - 32)
        F_C = str(F_C)
        # messagebox.showinfo("converted value", F)
        emma.config(text=F_C)

    elif from_type == "Fahrenheit" and to_type == "Kelvin":
        value = ema.get()
        F_K = 5 / 9 * (float(value) - 32) + 273
        F_K = str(F_K)
        emma.config(text=F_K)

    elif from_type == "Celsius" and to_type == "Kelvin":
        value = ema.get()
        C_K = (float(value)) + 273
        C_K = str(C_K)
        emma.config(text=C_K)

    elif from_type == "Kelvin" and to_type == "Celsius":
        value = ema.get()
        K_C = (float(value)) - 273
        K_C = str(K_C)
        emma.config(text=K_C)

    elif from_type == "Kelvin" and to_type == "Fahrenheit":
        value = ema.get()
        K_F = 9 / 5 * (float(value) - 273) + 32
        K_F = str(K_F)
        emma.config(text=K_F)

    else:
        # celsius to fahrenheit
        value = ema.get()
        C_F = 9/5 * (float(value) - 32)
        C_F = str(C_F)
        emma.config(text=C_F)

# menus
options= [
    "Fahrenheit",
    "Celsius",
    "Kelvin"]

clicked = StringVar()
clicked.set(options[0])

pressed = StringVar()
pressed.set(options[0])

From = OptionMenu(root, clicked, *options)
From.grid(row=1,column=1,padx=10)
To = OptionMenu(root, pressed, *options)
To.grid(row=3,column=1,pady=10)
myButton = Button(root, text="Convert",bg="#720a33",fg="white",command=show).grid(row=1,column=3)

# ENTRY AND DISPLAY
ema = Entry(root, fg="white", bg="#720a33",width=15)
ema.grid(row=1, column=2)
emma = Label(root, fg="white", bg="#720a33", text="Degree",padx=25)
emma.grid(row=3, column=2)

root.mainloop()