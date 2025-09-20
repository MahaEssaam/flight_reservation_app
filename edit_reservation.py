import tkinter as tk
from tkinter import messagebox
import database as db

def open_edit_window(parent, res_id, values):
    edit_win = tk.Toplevel(parent)
    edit_win.title(f"Edit Reservation {res_id}")
    edit_win.geometry("400x400")
    edit_win.configure(bg="#f0f4f7")

    tk.Label(
        edit_win, 
        text=f"Edit Reservation {res_id}", 
        font=("Arial", 14, "bold"), 
        bg="#f0f4f7", 
        fg="#1a237e"
    ).pack(pady=15)

    frame = tk.Frame(edit_win, bg="#f0f4f7")
    frame.pack(pady=10)

    labels = ["Name","Flight Number","Departure","Destination","Date","Seat Number"]
    entries = {}

    for i, lab in enumerate(labels):
        tk.Label(frame, text=lab + ":", font=("Arial", 11), bg="#f0f4f7").grid(
            row=i, column=0, sticky="w", padx=10, pady=5
        )
        e = tk.Entry(frame, font=("Arial", 11), width=25)
        e.grid(row=i, column=1, padx=10, pady=5)
        e.insert(0, values[i+1])  
        entries[lab] = e

    def update():
        data = {
            'name': entries["Name"].get(),
            'flight_number': entries["Flight Number"].get(),
            'departure': entries["Departure"].get(),
            'destination': entries["Destination"].get(),
            'date': entries["Date"].get(),
            'seat_number': entries["Seat Number"].get()
        }
        db.update_reservation(res_id, data)
        messagebox.showinfo("Success", f"Reservation {res_id} updated")
        edit_win.destroy()
        parent.destroy()

    tk.Button(
        edit_win, text="Update", 
        font=("Arial", 12, "bold"), 
        bg="#4CAF50", fg="white", width=20,
        command=update
    ).pack(pady=15)
