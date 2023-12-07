import tkinter as tk

def calculate():
    initial_concentration = float(initial_concentration_entry.get())
    final_concentration = float(final_concentration_entry.get())
    final_volume = float(final_volume_entry.get())

    initial_volume = (final_concentration * final_volume) / initial_concentration
    stock_volume_label.config(text=f"Initial volume of stock solution needed: {initial_volume:.2f} uL")

    diluent_volume = final_volume - initial_volume
    diluent_volume_label.config(text=f"Volume of dilutent to mix with stock solution: {diluent_volume:.2f} mL")

window = tk.Tk()
window.title("Dilution Calculator")

initial_concentration_label = tk.Label(window, text="Initial Concentration (M):")
initial_concentration_label.grid(row=0, column=0)

initial_concentration_entry = tk.Entry(window)
initial_concentration_entry.grid(row=0, column=1)

initial_volume_label = tk.Label(window, text="Initial Volume (uL):")
initial_volume_label.grid(row=1, column=0)

initial_volume_entry = tk.Entry(window)
initial_volume_entry.grid(row=1, column=1)

final_concentration_label = tk.Label(window, text="Final Concentration (M):")
final_concentration_label.grid(row=2, column=0)

final_concentration_entry = tk.Entry(window)
final_concentration_entry.grid(row=2, column=1)

final_volume_label = tk.Label(window, text="Final Volume (uL):")
final_volume_label.grid(row=3, column=0)

final_volume_entry = tk.Entry(window)
final_volume_entry.grid(row=3, column=1)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0)

stock_volume_label = tk.Label(window, text="")
stock_volume_label.grid(row=5, column=0)

diluent_volume_label = tk.Label(window, text="")
diluent_volume_label.grid(row=6, column=0)

window.mainloop()