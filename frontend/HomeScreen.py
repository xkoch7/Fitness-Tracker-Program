#function to acces the tracking screen in order to effectively track workouts (currently working on)
def openTrackingScreen():
    from vars import changeScreen
    changeScreen(4) 
    
#function to acces the home screen main ui to access all info (currently working on)
def openHistoryScreen(root,tk):
    underConst=tk.Label(root, text="Home Screen - Under Construction", font=("Helvetica", 16))
    underConst.grid(column=1, row=6)
    root.after(2000, lambda: underConst.grid_forget())  
    
#function to open settings screen implemented to add a more personal touch to the program (currently working on)
def openSettingsScreen(root,tk):
    underConst=tk.Label(root, text="Settings Screen - Under Construction", font=("Helvetica", 16)) 
    # dont put pack on same line makes the var a NoneType
    underConst.grid(column=1, row=7)
    root.after(2000, lambda: underConst.grid_forget())  
    
def logUserOut():
    from vars import changeScreen, email
    email =''
    changeScreen(0) 
    
#function to set up all buttons and labels actually adding something to the visuals and functionality
# returns list of widgets that get deleted on screen change
def setup(root,tk) -> list:
    welcomeLabel=tk.Label(root, text="Welcome to T&X Fitness", font=("Helvetica", 16))
    welcomeLabel.grid(column=1, row=0, pady=20, padx=100)
    trackBtn = tk.Button(root, text="Track Workout", width=20, height=2,command=lambda: openTrackingScreen())
    trackBtn.grid(column=1, row=2, pady=10, padx=100)
    historyBtn = tk.Button(root, text="View History", width=20, height=2, command=lambda: openHistoryScreen(root,tk))
    historyBtn.grid(column=1, row=3, pady=10, padx=100)
    settingsBtn = tk.Button(root, text="Settings", width=20, height=2, command=lambda: openSettingsScreen(root,tk))
    settingsBtn.grid(column=1, row=4, pady=10, padx=100)
    logOutBtn = tk.Button(root, text="Log Out", width=20, height=2, command = lambda:logUserOut())
    logOutBtn.grid(column=1, row=5, pady=10, padx=100)
    return [trackBtn, historyBtn, settingsBtn, logOutBtn]
    

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()