import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

import tkinter as tk
from PIL import ImageTk, Image
from Backend.GetInfo import getInfo
root = tk.Tk()
root.title("T&X Fitness")
# Set the window size to 500 pixels wide by 850 high
root.geometry("500x850")
image_path = "frontend\Images\GymLogo.png"
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)
image_label = tk.Label(root, image=tk_image)
image_label.image = tk_image

def handle_login():
    email = email_var.get()
    password = pass_var.get()
    getInfo(email, password)

email_var = tk.StringVar()
pass_var = tk.StringVar()

email_label = tk.Label(root, text = "Enter email:", font=("calibre", 10,"normal"))

email_entry = tk.Entry(root, textvariable = email_var, font=("calibre", 10,"normal"))

pass_label = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

pass_entry = tk.Entry(root, textvariable = pass_var, font=("calibre", 10,"normal"), show="*")

login_btn = tk.Button(root, text = "Login King", command = handle_login)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)
pass_label.grid(row=2, column=0)
pass_entry.grid(row=2, column=1)
image_label.grid(row=1, column=0)

login_btn.grid(row=2, column=1)

root.mainloop()