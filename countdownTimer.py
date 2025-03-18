#Create a Countdown Timer Using Python
import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        # Get time in seconds from user input
        countdown_time = int(entry.get())
        while countdown_time > 0:
            mins, secs = divmod(countdown_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=timer)
            root.update()
            time.sleep(1)
            countdown_time -= 1
        label.config(text="00:00")
        messagebox.showinfo("Time's up!", "Countdown Finished!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create GUI window
root = tk.Tk()
root.title("Countdown Timer")

# GUI elements
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(pady=10)

start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Arial", 15))
start_button.pack(pady=5)

label = tk.Label(root, text="00:00", font=("Arial", 40))
label.pack(pady=20)

# Run the app
root.mainloop()
