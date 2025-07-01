# Import necessary files
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Entry box for new tasks
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Function to add tasks
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update tasks
def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Function to remove tasks
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=25, height=10)
listbox.pack(pady=10)

# Start the main event loop
root.mainloop()