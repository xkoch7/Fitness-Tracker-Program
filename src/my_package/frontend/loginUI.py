
from PIL import ImageTk, Image
import sys
import os
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Backend.GetInfo import  getInfo

#function to check if inputed email matches the saved list along with the cooresponding password
#if not correct asks user to try again or create account
def handleLogin(email_var, pass_var, root, tk):
    email = email_var.get()
    password = pass_var.get()
    if not email or not password:
        temp=tk.Label(root, text="Please enter both email and password.", font=("Helvetica", 10),fg="red")
        temp.grid(row=3, column = 2)
        root.after(2000, lambda: temp.grid_forget())
        return False
    
    # verify login info
    if getInfo(email, password):
        import my_package.vars as vars
        vars.changeScreen(3)  # Move to HomeScreen
        vars.email = email
        
    else:
        temp=tk.Label(root, text="Invalid email or password. Please try again.", font=("Helvetica", 10),fg="red")
        temp.grid(row=3, column = 2)
        root.after(2000, lambda: temp.grid_forget())
        return False
    
def createAccScreen():
    from my_package.vars import changeScreen
    changeScreen(2)  # Move to create account screen

#setup function to display all buttons and labels and make program functional
# returns list of widgets that get deleted on screen change
def setup(root,tk) -> list:
    root.grid_columnconfigure(0, weight=1)
    emailVar = tk.StringVar()
    passVar = tk.StringVar()
    infoLabel = tk.Label(root, text="Welcome to X&T Fitness! Please log in or create an account to continue.", font=("Helvetica", 13), wraplength=400, justify="center")    
    emailLabel = tk.Label(root, text = "Enter email:", font=("calibre", 10,"normal"))

    emailEntry = tk.Entry(root, textvariable = emailVar, font=("calibre", 10,"normal"))

    passLabel = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    passEntry = tk.Entry(root, textvariable = passVar, font=("calibre", 10,"normal"), show="*")

    loginBtn = tk.Button(root, text = "Login King", command = lambda: handleLogin(emailVar, passVar, root, tk))

    createAccBtn = tk.Button(root, text = "Create Account", command = lambda: createAccScreen())

    imagePath = "src\\my_package\\frontend\\Images\\GymLogo.png" 
    pil_image = Image.open(imagePath)
    newWidth = 250
    newHeight = 250
    resizedImage = pil_image.resize((newWidth, newHeight), Image.Resampling.LANCZOS)
    tkImage = ImageTk.PhotoImage(resizedImage)
    imageLabel = tk.Label(root, image=tkImage)
    setattr(imageLabel, 'image', tkImage) 
    
    imageLabel.grid(row=0, column = 2,sticky='W')
    infoLabel.grid(row=1, column = 1, columnspan= 2, padx= 50)
    emailLabel.grid(row=2, column = 1)
    emailEntry.grid(row=2, column = 2)
    passLabel.grid(row=3, column = 1)
    passEntry.grid(row=3, column = 2)
    loginBtn.grid(row=4, column = 2)
    createAccBtn.grid(row=5, column = 2)
    return [emailLabel, emailEntry, passLabel, passEntry, loginBtn, imageLabel, createAccBtn]

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()