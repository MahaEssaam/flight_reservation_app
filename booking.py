import tkinter as tk
from tkinter import messagebox
import database as db

def open_booking_window(root):
    win = tk.Toplevel(root)
    win.title("Book a Flight ")
    win.geometry("400x400")
    win.configure(bg="#f0f4f7") 

    tk.Label(win, text="Enter Flight Details", 
             font=("Arial", 14, "bold"), bg="#f0f4f7").pack(pady=15)

    frame = tk.Frame(win, bg="#f0f4f7")
    frame.pack(pady=10)

    labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
    entries = {}

    for i, lab in enumerate(labels):
        tk.Label(frame, text=lab + ":", font=("Arial", 11), bg="#f0f4f7").grid(row=i, column=0, sticky="w", padx=10, pady=5)
        e = tk.Entry(frame, font=("Arial", 11), width=25)
        e.grid(row=i, column=1, padx=10, pady=5)
        entries[lab] = e

    def submit():
        data = {
            'name': entries["Name"].get(),
            'flight_number': entries["Flight Number"].get(),
            'departure': entries["Departure"].get(),
            'destination': entries["Destination"].get(),
            'date': entries["Date"].get(),
            'seat_number': entries["Seat Number"].get()
        }
        if not data['name'] or not data['flight_number']:
            messagebox.showerror("Error", "Name and Flight Number are required")
            return
        db.add_reservation(data)
        messagebox.showinfo("Success", "Reservation Added Successfully")
        win.destroy()

    tk.Button(win, text="Submit",font=("Arial", 12, "bold"), 
              bg="#1a73e8", fg="white", width=20, command=submit).pack(pady=15)
