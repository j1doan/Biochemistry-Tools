import tkinter as tk
from tkinter import messagebox

def calculate_dilutions():
    try:
        num_dilutions = int(num_dilutions_entry.get())
        dilution_ratio = float(dilution_ratio_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for dilutions and ratio.")
        return

    result = "1"
    for i in range(num_dilutions):
        result += f" -> 1:{dilution_ratio**(i+1)}"
    
    result_label.config(text=result)

root = tk.Tk()
root.title("Serial Dilution Calculator")

num_dilutions_label = tk.Label(root, text="Number of dilutions:")
num_dilutions_label.pack()

num_dilutions_entry = tk.Entry(root)
num_dilutions_entry.pack()

dilution_ratio_label = tk.Label(root, text="Dilution ratio:")
dilution_ratio_label.pack()

dilution_ratio_entry = tk.Entry(root)
dilution_ratio_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_dilutions)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()