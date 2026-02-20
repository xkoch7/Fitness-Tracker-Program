
import tkinter  as tk
screen=1
root = tk.Tk()
root.title("T&X Fitness")
# Set the window size to 500 pixels wide by 850 high
root.geometry("500x850")
widgets=[]
email=""
index=0
def changeScreen(newScreen: int) -> None:
    global screen, widgets,root
    screen = newScreen  # Move to the new screen
    for widget in widgets:
        widget.grid_forget()
    root.quit()