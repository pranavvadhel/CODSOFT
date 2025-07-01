import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

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

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

listbox = tk.Listbox(root, width=25, height=10)
listbox.pack(pady=10)

root.mainloop()