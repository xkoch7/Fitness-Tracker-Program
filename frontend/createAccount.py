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
    vars.screen = 2  # Move to HomeScreen
    for widget in vars.widgets:
        widget.grid_forget()

    root.quit()
    



def setup(root,tk) -> list:
    email_var = tk.StringVar()
    pass_var1 = tk.StringVar()
    pass_var2 = tk.StringVar()
    pass_var = tk.StringVar()
    email_label = tk.Label(root, text = "Enter email:", font=("calibre", 10,"normal"))

    email_entry = tk.Entry(root, textvariable = email_var, font=("calibre", 10,"normal"))

    pass_label1 = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    pass_entry1 = tk.Entry(root, textvariable = pass_var1, font=("calibre", 10,"normal"), show="*")

    pass_label2 = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    pass_entry2 = tk.Entry(root, textvariable = pass_var2, font=("calibre", 10,"normal"), show="*")

    createAcc_btn = tk.Button(root, text = "Create Account", command = lambda: handleAcc(email_var, pass_var1, pass_var2, root, tk))

    email_label.grid(row=1, column=0)
    email_entry.grid(row=1, column=1)
    pass_label1.grid(row=2, column=0)
    pass_entry1.grid(row=2, column=1)
    pass_label2.grid(row=3, column=0)
    pass_entry2.grid(row=3, column=1)
    createAcc_btn.grid(row=4, column=1)

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()