import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
def copy_password():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password to copy")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")
password_var = tk.StringVar()
length_var = tk.IntVar(value=12)
title = tk.Label(root, text="Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)
length_label = t_
