import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(temp_entry.get())
        unit = unit_var.get()
    except ValueError:
        messagebox.showerror("ERROR", "Please enter a valid number for temperature.")
        return

    if unit == "Fahrenheit (°F)":
        celsius = (temp - 32) * 5/9
        kelvin = (temp + 459.67) * 5/9
        result = f"{temp}°F = {celsius:.2f}°C = {kelvin:.2f} K"
    elif unit == "Celsius (°C)":
        fahrenheit = temp * 9/5 + 32
        kelvin = temp + 273.15
        result = f"{temp}°C = {fahrenheit:.2f}°F = {kelvin:.2f} K"
    else:  # unit == "Kelvin (K)"
        celsius = temp - 273.15
        fahrenheit = temp * 9/5 - 459.67
        result = f"{temp} K = {celsius:.2f}°C = {fahrenheit:.2f}°F"
    
    result_label.config(text=result)

root = tk.Tk()
root.title("Temperature Converter")

temp_label = tk.Label(root, text="Temperature:")
temp_label.pack()

temp_entry = tk.Entry(root)
temp_entry.pack()

unit_var = tk.StringVar(root)
unit_var.set("Fahrenheit (°F)")  # default value

unit_optionmenu = tk.OptionMenu(root, unit_var, "Fahrenheit (°F)", "Celsius (°C)", "Kelvin (K)")
unit_optionmenu.pack()

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()