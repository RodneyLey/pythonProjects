import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "employees.json"

# Load employee data from file
def load_records():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save employee data to file
def save_records(records):
    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)

# Add a new employee
def add_employee(records, name):
    if name in records:
        messagebox.showinfo("Info", f"{name} already exists.")
    else:
        records[name] = []
        messagebox.showinfo("Success", f"{name} has been added.")

# Clock in
def clock_in(records, name):
    if name not in records:
        messagebox.showwarning("Warning", f"Employee '{name}' does not exist. Add them first.")
        return
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    records[name].append({"clock_in": now, "clock_out": "Not yet clocked out"})
    messagebox.showinfo("Clock In", f"{name} clocked in at {now}")

# Clock out
def clock_out(records, name):
    if name not in records or not records[name]:
        messagebox.showwarning("Warning", f"No clock-in record found for {name}.")
        return
    last_entry = records[name][-1]
    if last_entry["clock_out"] == "Not yet clocked out":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_entry["clock_out"] = now
        messagebox.showinfo("Clock Out", f"{name} clocked out at {now}")
    else:
        messagebox.showinfo("Info", f"{name} has already clocked out. Please clock in again.")

# Show records window
def show_records(records):
    top = tk.Toplevel()
    top.title("Employee Records")
    text = tk.Text(top, wrap=tk.WORD, width=80, height=25)
    text.pack()
    for name, history in records.items():
        text.insert(tk.END, f"\nEmployee: {name}\n")
        for idx, entry in enumerate(history, start=1):
            text.insert(tk.END, f"  Entry {idx}: Clock In: {entry['clock_in']} | Clock Out: {entry['clock_out']}\n")

# Display employees with search functionality
def show_employee_list(records):
    def update_list():
        search_query = search_var.get().lower()
        listbox.delete(0, tk.END)
        for name in records.keys():
            if search_query in name.lower():
                listbox.insert(tk.END, name)

    def clock_in_selected():
        selected = listbox.get(tk.ACTIVE)
        if selected:
            clock_in(records, selected)

    def clock_out_selected():
        selected = listbox.get(tk.ACTIVE)
        if selected:
            clock_out(records, selected)

    top = tk.Toplevel()
    top.title("Saved Employees")

    search_var = tk.StringVar()
    search_var.trace("w", lambda name, index, mode: update_list())

    search_entry = tk.Entry(top, textvariable=search_var, width=40)
    search_entry.pack(padx=10, pady=5)
    search_entry.insert(0, "Search employee...")

    listbox = tk.Listbox(top, width=40, height=15)
    listbox.pack(padx=10, pady=10)

    for name in records.keys():
        listbox.insert(tk.END, name)

    tk.Button(top, text="Clock In", command=clock_in_selected).pack(pady=5)
    tk.Button(top, text="Clock Out", command=clock_out_selected).pack(pady=5)

# GUI Setup
def run_gui():
    records = load_records()

    root = tk.Tk()
    root.title("Employee Time Tracker")

    def add_emp():
        name = simpledialog.askstring("Add Employee", "Enter employee name:")
        if name:
            add_employee(records, name)

    def view_records():
        show_records(records)

    def show_employees():
        show_employee_list(records)

    def save_and_exit():
        save_records(records)
        root.destroy()

    tk.Button(root, text="Add New Employee", command=add_emp, width=30).pack(pady=5)
    tk.Button(root, text="Saved Employees (Search & Clock In/Out)", command=show_employees, width=30).pack(pady=5)
    tk.Button(root, text="View All Records", command=view_records, width=30).pack(pady=5)
    tk.Button(root, text="Save and Exit", command=save_and_exit, width=30).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
