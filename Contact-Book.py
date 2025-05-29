import tkinter as tk
from tkinter import messagebox, simpledialog
contacts = []
def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    address = address_text.get("1.0", "end").strip()
    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and phone are required.")
        return
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()
    refresh_contact_list()
def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for index, contact in enumerate(contacts):
        contact_listbox.insert(tk.END, f"{index+1}. {contact['name']} - {contact['phone']}")
def show_selected_contact(event):
    if not contact_listbox.curselection():
        return
    index = contact_listbox.curselection()[0]
    contact = contacts[index]
    name_var.set(contact['name'])
    phone_var.set(contact['phone'])
    email_var.set(contact['email'])
    address_text.delete("1.0", "end")
    address_text.insert("1.0", contact['address'])
def search_contact():
    query = search_var.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone']:
            contact_listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")
def update_contact():
    if not contact_listbox.curselection():
        messagebox.showwarning("Select Contact", "Select a contact to update.")
        return
    index = contact_listbox.curselection()[0]
    contacts[index] = {
        'name': name_var.get().strip(),
        'phone': phone_var.get().strip(),
        'email': email_var.get().strip(),
        'address': address_text.get("1.0", "end").strip()
    }
    messagebox.showinfo("Updated", "Contact updated successfully!")
    refresh_contact_list()
    clear_fields()
def delete_contact():
    if not contact_listbox.curselection():
        messagebox.showwarning("Select Contact", "Select a contact to delete.")
        return
    index = contact_listbox.curselection()[0]
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
    if confirm:
        contacts.pop(index)
        refresh_contact_list()
        clear_fields()
def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_text.delete("1.0", "end")
root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x500")
root.config(bg="#f5f5f5")
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
search_var = tk.StringVar()
tk.Label(root, text="Contact Manager", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)
form_frame = tk.Frame(root, bg="#f5f5f5")
form_frame.pack(pady=5)
tk.Label(form_frame, text="Name:", bg="#f5f5f5").grid(row=0, column=0, sticky="e")
tk.Entry(form_frame, textvariable=name_var, width=30).grid(row=0, column=1, padx=5, pady=2)
tk.Label(form_frame, text="Phone:", bg="#f5f5f5").grid(row=1, column=0, sticky="e")
tk.Entry(form_frame, textvariable=phone_var, width=30).grid(row=1, column=1, padx=5, pady=2)
tk.Label(form_frame, text="Email:", bg="#f5f5f5").grid(row=2, column=0, sticky="e")
tk.Entry(form_frame, textvariable=email_var, width=30).grid(row=2, column=1, padx=5, pady=2)
tk.Label(form_frame, text="Address:", bg="#f5f5f5").grid(row=3, column=0, sticky="ne")
address_text = tk.Text(form_frame, height=4, width=30)
address_text.grid(row=3, column=1, padx=5, pady=2)
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", width=10, command=clear_fields).grid(row=0, column=3, padx=5)
tk.Entry(root, textvariable=search_var, width=30).pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack(pady=2)
contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", show_selected_contact)
refresh_contact_list()
root.mainloop()
