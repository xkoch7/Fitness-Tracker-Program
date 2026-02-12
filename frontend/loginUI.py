
from PIL import ImageTk, Image
from Backend.GetInfo import getInfo


#function to check if inputed email matches the saved list along with the cooresponding password
#if not correct asks user to try again or create account
def handleLogin(email_var, pass_var, root, tk):
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
        vars.email = email
        for widget in vars.widgets:
            widget.grid_forget()
        root.quit()  # Exit the mainloop to refresh the screen
        
    else:
        temp=tk.Label(root, text="Invalid email or password. Please try again.", font=("Helvetica", 10),fg="red")
        temp.grid(row=3, column=1)
        root.after(2000, lambda: temp.grid_forget())
        return False
    
def createAccScreen():
    from vars import changeScreen
    changeScreen(2)  # Move to create account screen

#setup function to display all buttons and labels and make program functional
# returns list of widgets that get deleted on screen change
def setup(root,tk) -> list:
    emailVar = tk.StringVar()
    passVar = tk.StringVar()

    emailLabel = tk.Label(root, text = "Enter email:", font=("calibre", 10,"normal"))

    emailEntry = tk.Entry(root, textvariable = emailVar, font=("calibre", 10,"normal"))

    passLabel = tk.Label(root, text = "Enter password:", font=("calibre", 10,"normal"))

    passEntry = tk.Entry(root, textvariable = passVar, font=("calibre", 10,"normal"), show="*")

    loginBtn = tk.Button(root, text = "Login King", command = lambda: handleLogin(emailVar, passVar, root, tk))

    createAccBtn = tk.Button(root, text = "Create Account", command = lambda: createAccScreen())

    imagePath = "frontend\\Images\\GymLogo.png" 
    pil_image = Image.open(imagePath)
    newWidth = 250
    newHeight = 250
    resizedImage = pil_image.resize((newWidth, newHeight), Image.Resampling.LANCZOS)
    tkImage = ImageTk.PhotoImage(resizedImage)
    imageLabel = tk.Label(root, image=tkImage)
    setattr(imageLabel, 'image', tkImage) 

    emailLabel.grid(row=1, column=0)
    emailEntry.grid(row=1, column=1)
    passLabel.grid(row=2, column=0)
    passEntry.grid(row=2, column=1)
    imageLabel.grid(row=0, column=1)
    loginBtn.grid(row=4, column=1)
    createAccBtn.grid(row=6, column=1)
    return [emailLabel, emailEntry, passLabel, passEntry, loginBtn, imageLabel, createAccBtn]

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()