#function to acces the tracking screen in order to effectively track workouts (currently working on)
def open_tracking_screen(root,tk):
    temp=tk.Label(root, text="Tracking Screen - Under Construction", font=("Helvetica", 16))
    temp.grid(column=1, row=5)
    root.after(2000, lambda: temp.grid_forget())
#function to acces the history screen main ui to access all info (currently working on)
def open_history_screen(root,tk):
    temp=tk.Label(root, text="History Screen - Under Construction", font=("Helvetica", 16))
    temp.grid(column=1, row=6)
    root.after(2000, lambda: temp.grid_forget())  
#function to open settings screen implemented to add a more personal touch to the program (currently working on)
def open_settings_screen(root,tk):
    temp=tk.Label(root, text="Settings Screen - Under Construction", font=("Helvetica", 16)) 
    # dont put pack on same line makes the var a NoneType
    temp.grid(column=1, row=7)
    root.after(2000, lambda: temp.grid_forget())  
     
#function to set up all buttons and labels actually adding something to the visuals and functionality
# returns list of widgets that get deleted on screen change
def setup(root,tk) -> list:
    welcome_label=tk.Label(root, text="Welcome to T&X Fitness", font=("Helvetica", 16))
    welcome_label.grid(column=1, row=0, pady=20, padx=100)
    track_btn = tk.Button(root, text="Track Workout", width=20, height=2,command=lambda: open_tracking_screen(root,tk))
    track_btn.grid(column=1, row=2,padx=100, pady=10)
    history_btn = tk.Button(root, text="View History", width=20, height=2, command=lambda: open_history_screen(root,tk))
    history_btn.grid(column=1, row=3, pady=10,padx=100)
    settings_btn = tk.Button(root, text="Settings", width=20, height=2,command=lambda: open_settings_screen(root,tk))
    settings_btn.grid(column=1, row=4, pady=10,padx=100)
    return [track_btn, history_btn, settings_btn]
    

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()