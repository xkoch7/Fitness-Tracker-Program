import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
from vars import root, tk
def open_tracking_screen():
    temp=tk.Label(root, text="Tracking Screen - Under Construction", font=("Helvetica", 16))
    temp.pack(pady=20)
    root.after(2000, lambda: temp.pack_forget())
def open_home_screen():
    temp=tk.Label(root, text="Home Screen - Under Construction", font=("Helvetica", 16))
    temp.pack(pady=20)
    root.after(2000, lambda: temp.pack_forget())  
def open_settings_screen():
    temp=tk.Label(root, text="Settings Screen - Under Construction", font=("Helvetica", 16)) 
    # dont put pack on same line makes the var a NoneType
    temp.pack(pady=20)
    root.after(2000, lambda: temp.pack_forget())  
     
    
tk.Label(root, text="Welcome to T&X Fitness", font=("Helvetica", 16)).pack(pady=20)
track_btn = tk.Button(root, text="Track Workout", width=20, height=2,command=open_tracking_screen).pack(pady=10)
history_btn = tk.Button(root, text="View History", width=20, height=2, command=open_home_screen).pack(pady=10)
settings_btn = tk.Button(root, text="Settings", width=20, height=2,command=open_settings_screen).pack(pady=10)

root.mainloop()