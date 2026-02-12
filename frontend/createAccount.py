from Backend.GetInfo import createAcc

#function that hadnles the creation of an account so a user can sign up for program
def handleAcc(email_var, pass_var1, pass_var2, root, tk):
    if pass_var1.get() != pass_var2.get():
        temp_label = tk.Label(root, text="Passwords do not match please try again", font=("calibre", 10, "normal"))
        temp_label.grid(row=5, column=1)
        return

    email = email_var.get()
    password = pass_var1.get()

    createAcc(email, password)

    import vars
    vars.email = email
    vars.screen = 2  # Move to HomeScreen
    for widget in vars.widgets:
        widget.grid_forget()

    root.quit()
    



def setup(root,tk) -> list:
    emailVar = tk.StringVar()
    passVar1 = tk.StringVar()
    passVar2 = tk.StringVar()
    pass_var = tk.StringVar()
    emailLabel = tk.Label(root, text = "Enter email:", font=("calibre", 10,"normal"))

    emailEntry = tk.Entry(root, textvariable = emailVar, font=("calibre", 10,"normal"))

    passLabel1 = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    passEntry1 = tk.Entry(root, textvariable = passVar1, font=("calibre", 10,"normal"), show="*")

    passLabel2 = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    passEntry2 = tk.Entry(root, textvariable = passVar2, font=("calibre", 10,"normal"), show="*")

    createAccBtn = tk.Button(root, text = "Create Account", command = lambda: handleAcc(emailVar, passVar1, passVar2, root, tk))

    emailLabel.grid(row=1, column=0)
    emailEntry.grid(row=1, column=1)
    passLabel1.grid(row=2, column=0)
    passEntry1.grid(row=2, column=1)
    passLabel2.grid(row=3, column=0)
    passEntry2.grid(row=3, column=1)
    createAccBtn.grid(row=4, column=1)
    return [emailLabel, emailEntry, passLabel1, passEntry1, passLabel2, passEntry2, createAccBtn]

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()