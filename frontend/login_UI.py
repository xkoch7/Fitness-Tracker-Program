
from PIL import ImageTk, Image
from Backend.GetInfo import getInfo



def handle_login(email_var, pass_var, root, tk):
    email = email_var.get()
    password = pass_var.get()
    if not email or not password:
        temp=tk.Label(root, text="Please enter both email and password.", font=("Helvetica", 10),fg="red")
        temp.grid(row=3, column=1)
        root.after(2000, lambda: temp.grid_forget())
        return False
    # verify login info
    if getInfo(email, password):
        import vars
        vars.screen = 2  # Move to HomeScreen
        for widget in vars.widgets:
            widget.grid_forget()
        root.quit()  # Exit the mainloop to refresh the screen
    else:
        temp=tk.Label(root, text="Invalid email or password. Please try again.", font=("Helvetica", 10),fg="red")
        temp.grid(row=3, column=1)
        root.after(2000, lambda: temp.grid_forget())
        return False
    
def setup(root,tk) -> list:
    email_var = tk.StringVar()
    pass_var = tk.StringVar()

    email_label = tk.Label(root, text = "Enter email:", font=("calibre", 10,"normal"))

    email_entry = tk.Entry(root, textvariable = email_var, font=("calibre", 10,"normal"))

    pass_label = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    pass_entry = tk.Entry(root, textvariable = pass_var, font=("calibre", 10,"normal"), show="*")

    login_btn = tk.Button(root, text = "Login King", command = lambda: handle_login(email_var, pass_var, root, tk))

    image_path = "frontend\\Images\\GymLogo.png" 
    pil_image = Image.open(image_path)
    new_width = 250
    new_height = 250
    resized_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(root, image=tk_image)
    setattr(image_label, 'image', tk_image) 

    email_label.grid(row=1, column=0)
    email_entry.grid(row=1, column=1)
    pass_label.grid(row=2, column=0)
    pass_entry.grid(row=2, column=1)
    image_label.grid(row=0, column=1)
    login_btn.grid(row=4, column=1)
    return [email_label, email_entry, pass_label, pass_entry, login_btn, image_label]
if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()