import threading
import time
import json

def add_workout(root, tk,workout):
    import vars
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        data['workoutData'][vars.email][workout] = {}
    
    with open('Backend\\UserInfo.json', 'w') as f:
        json.dump(data, f, indent=4)

def update_workout_list(root, tk, muscleGroupValue):
    while True:
        workout=tk.StringVar(value='Select Workout')
        addWorkout_btn = tk.Button(root, text="Add Workout", width=20, height=2,command=lambda: add_workout(root,tk,workout.get()))
        subOpMenu=tk.OptionMenu(root,workout, 'Select Workout',[])
        
        while muscleGroupValue.get() != "Select Group":
            print(muscleGroupValue.get())
            workout_options = {
                'Chest': ['Bench Press', 'Incline Dumbbell Press', 'Chest Fly'],
                'Back': ['Pull-ups', 'Deadlifts', 'Bent-over Rows'],
                'Legs': ['Squats', 'Lunges', 'Leg Press'],
                'Arms': ['Bicep Curls', 'Tricep Dips', 'Hammer Curls']
            }
            specWorkouts = workout_options.get(muscleGroupValue.get(), [])
            subOpMenu=tk.OptionMenu(root,workout,'Select Workout',*specWorkouts)
            addWorkout_btn.grid(column=1, row=2,padx=100, pady=10)
            subOpMenu.grid(column=1, row=3,padx=100, pady=10)        
            time.sleep(.25) 
        subOpMenu.grid_forget()
        addWorkout_btn.grid_forget()
        
def setup(root,tk) -> list:
    
    muscleGroup=tk.StringVar(value='Select Group')
    
    update_workouts=threading.Thread(target=update_workout_list, args=(root, tk, muscleGroup)) 
    update_workouts.start()
    welcome_label=tk.Label(root, text="Welcome to T&X Fitness", font=("Helvetica", 16))
    welcome_label.grid(column=1, row=0, pady=20, padx=100)
    opMenu=tk.OptionMenu(root,muscleGroup,  'Chest', 'Back', 'Legs', 'Arms', 'Cardio', 'Core/Abs', "Shoulders")
    opMenu.grid(column=1, row=1, pady=10)
    
    
    # history_btn = tk.Button(root, text="View History", width=20, height=2, command=lambda: open_history_screen(root,tk))
    # history_btn.grid(column=1, row=3, pady=10,padx=100)
    # settings_btn = tk.Button(root, text="Settings", width=20, height=2,command=lambda: open_settings_screen(root,tk))
    # settings_btn.grid(column=1, row=4, pady=10,padx=100)
    return [opMenu]

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()