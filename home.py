import tkinter as tk
from booking import open_booking_window
from reservations import open_reservations_window

def home_screen(root):
    root.title("Flight Reservation App")
    root.geometry("450x250")
    root.configure(bg="#e8f0fe")

    title = tk.Label(root, text="Flight Reservation System", 
                     font=("Arial", 16, "bold"), bg="#e8f0fe", fg="#1a237e")
    title.pack(pady=20)

    btn_style = {"font": ("Arial", 12, "bold"), "bg": "#1a73e8", "fg": "white", "width": 20, "height": 2}

    tk.Button(root, text="Book Flight", command=lambda: open_booking_window(root), **btn_style).pack(pady=10)
    tk.Button(root, text="View Reservations", command=lambda: open_reservations_window(root), **btn_style).pack(pady=10)
