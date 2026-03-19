import sys
import os
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Backend.GetInfo import createAcc
#function that hadnles the creation of an account so a user can sign up for program
def handleAcc(emailVar, passVar1, passVar2, root, tk):
    if passVar1.get() != passVar2.get():
        notMatching = tk.Label(root, text="Passwords do not match please try again", font=("Helvetica", 10, "normal"))
        notMatching.grid(row=5, column = 2)
        return

    email = emailVar.get()
    password = passVar1.get()

    createAcc(email, password)

    from my_package.vars import changeScreen
    changeScreen(3)  # Move to home screen after account creation


def backToLogin():
    from my_package.vars import changeScreen
    changeScreen(1)  # Move to login screen

def setup(root,tk) -> list:
    root.grid_columnconfigure(0,weight = 1)
    root.grid_columnconfigure(3, weight= 1,pad=100)
    emailVar = tk.StringVar()
    passVar1 = tk.StringVar()
    passVar2 = tk.StringVar()
    infoLable = tk.Label(root, text="Create Account:", font=("Helvetica", 16, "bold"))
    emailLabel = tk.Label(root, text = "Enter email:", font=("Helvetica", 10,"normal"))

    emailEntry = tk.Entry(root, textvariable = emailVar, font=("Helvetica", 10,"normal"))

    passLabel1 = tk.Label(root, text = "Enter password:", font=("Helvetica", 10,"normal"))

    passEntry1 = tk.Entry(root, textvariable = passVar1, font=("Helvetica", 10,"normal"), show="*")

    passLabel2 = tk.Label(root, text = "Enter password:", font=("Helvetica", 10,"normal"))

    passEntry2 = tk.Entry(root, textvariable = passVar2, font=("Helvetica", 10,"normal"), show="*")

    createAccBtn = tk.Button(root, text = "Create Account", command = lambda: handleAcc(emailVar, passVar1, passVar2, root, tk))

    backBtn = tk.Button(root, text="Back to Login", command=lambda: backToLogin())
    infoLable.grid(row=0, column = 1, columnspan=2, pady=20)
    emailLabel.grid(row=1, column = 1)
    emailEntry.grid(row=1, column = 2)
    passLabel1.grid(row=2, column = 1)
    passEntry1.grid(row=2, column = 2)
    passLabel2.grid(row=3, column = 1)
    passEntry2.grid(row=3, column = 2)
    createAccBtn.grid(row=4, column = 2)
   
    backBtn.grid(row=5, column = 2)
    return [emailLabel, emailEntry, passLabel1, passEntry1, passLabel2, passEntry2, createAccBtn, backBtn]

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()