import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
root.resizable(False, False)
title_label = tk.Label(root, text="Application Password Generator", font=("Arial", 12))
title_label.pack(pady=10)
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
password_entry = tk.Entry(root, font=("Courier", 12), justify='center')
password_entry.pack(pady=5)
root.mainloop()
