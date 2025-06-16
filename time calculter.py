import tkinter as tk
from tkinter import messagebox

def calculate_time():
    try:
        total_seconds = int(entry_seconds.get())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        result = f"Total hours: {hours}\nTotal minutes: {minutes}\nRest seconds: {seconds}"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer number of seconds.")

root = tk.Tk()
root.title("Time Calculator")

tk.Label(root, text="Please enter total seconds:", font=("Arial", 14)).pack(pady=10)
entry_seconds = tk.Entry(root, font=("Arial", 14), width=20)
entry_seconds.pack(pady=5)

btn_calc = tk.Button(root, text="Calculate", font=("Arial", 14), bg="#4CAF50", fg="white", command=calculate_time)
btn_calc.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14), fg="#333")
label_result.pack(pady=20)

root.mainloop()