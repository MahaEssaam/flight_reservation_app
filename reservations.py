import tkinter as tk
from tkinter import ttk, messagebox
import database as db
from edit_reservation import open_edit_window

def open_reservations_window(root):
    win = tk.Toplevel(root)
    win.title("Reservations List")
    win.geometry("900x500")   
    win.configure(bg="#f0f4f7")

    tk.Label(
        win, text="All Reservations",
        font=("Arial", 14, "bold"),
        bg="#f0f4f7", fg="#1a237e"
    ).pack(pady=10)

    frame = tk.Frame(win, bg="#f0f4f7")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    cols = ("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number")
    tree = ttk.Treeview(frame, columns=cols, show="headings")

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
    style.configure("Treeview", font=("Arial", 10), rowheight=25)

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    reservations = db.get_all_reservations()
    for r in reservations:
        tree.insert("", "end", values=r)

    btn_frame = tk.Frame(win, bg="#f0f4f7")
    btn_frame.pack(pady=10)

    def delete_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a reservation to delete")
            return
        res_id = tree.item(selected_item)["values"][0]
        db.delete_reservation(res_id)
        tree.delete(selected_item)
        messagebox.showinfo("Success", f"Reservation {res_id} deleted")

    def edit_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a reservation to edit")
            return
        values = tree.item(selected_item)["values"]
        res_id = values[0]
        open_edit_window(win, res_id, values)

    edit_btn = tk.Button(
        btn_frame, text="Edit Selected",
        font=("Arial", 11, "bold"),
        bg="#ffc107", fg="black", width=18,
        command=edit_selected
    )
    edit_btn.grid(row=0, column=0, padx=15)

    delete_btn = tk.Button(
        btn_frame, text="Delete Selected",
        font=("Arial", 11, "bold"),
        bg="#e53935", fg="white", width=18,
        command=delete_selected
    )
    delete_btn.grid(row=0, column=1, padx=15)
