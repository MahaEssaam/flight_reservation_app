import tkinter as tk
import database as db
from home import home_screen

db.create_table()

root = tk.Tk()
home_screen(root)
root.mainloop()
