import os
import tkinter as tk

# Only create root if we aren't in a headless environment
if "DISPLAY" in os.environ or os.name == 'nt':
    root = tk.Tk()
else:
    root = None # Or a Mock object
root.title("T&X Fitness")
# Set the window size to 500 pixels wide by 850 high
root.geometry("500x850")
widgets=[]
email=""
index=0
screen=1

def changeScreen(newScreen: int) -> None:
    global screen
    screen = newScreen  # Move to the new screen
    for widget in widgets:
        widget.grid_forget()
    root.quit()