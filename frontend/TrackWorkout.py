import threading
import time
import json

def addWorkout(root, tk,workout):
    import vars
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        data['workoutData'][vars.email][workout] = {}
    
    with open('Backend\\UserInfo.json', 'w') as f:
        json.dump(data, f, indent=4)

def updateWorkoutList(root, tk, muscleGroupValue):
    while True:
        workout=tk.StringVar(value='Select Workout')
        reps= tk.StringVar(value='0')
        sets= tk.StringVar(value='0')
        weight= tk.StringVar(value='0')
        addWorkoutBtn = tk.Button(root, text="Add Workout", width=20, height=2,command=lambda: addWorkout(root,tk,workout.get()))
        subOpMenu=tk.OptionMenu(root,workout, 'Select Workout',[])
        repsEntry=tk.Entry(root, textvariable = reps, font=("calibre", 10,"normal"))
        setsEntry=tk.Entry(root, textvariable = sets, font=("calibre", 10,"normal"))
        weightEntry=tk.Entry(root, textvariable = weight, font=("calibre", 10,"normal"))

        while muscleGroupValue.get() != "Select Group":
            print(muscleGroupValue.get())
            workoutOptions = {
                'Chest': ['Bench Press', 'Incline Dumbbell Press', 'Chest Fly'],
                'Back': ['Pull-ups', 'Deadlifts', 'Bent-over Rows'],
                'Legs': ['Squats', 'Lunges', 'Leg Press'],
                'Arms': ['Bicep Curls', 'Tricep Dips', 'Hammer Curls']
            }
            specWorkouts = workoutOptions.get(muscleGroupValue.get(), [])
            subOpMenu=tk.OptionMenu(root,workout,'Select Workout',*specWorkouts)
            addWorkoutBtn.grid(column=1, row=2,padx=100, pady=10)
            subOpMenu.grid(column=1, row=3,padx=100, pady=10)        
            time.sleep(.25) 
        subOpMenu.grid_forget()
        addWorkoutBtn.grid_forget()
        repsEntry.grid_forget()
        setsEntry.grid_forget()
        weightEntry.grid_forget()

def setup(root,tk) -> list:
    
    muscleGroup=tk.StringVar(value='Select Group')
    
    updateWorkouts=threading.Thread(target=updateWorkoutList, args=(root, tk, muscleGroup)) 
    updateWorkouts.start()
    welcomeLabel=tk.Label(root, text="Welcome to T&X Fitness", font=("Helvetica", 16))
    welcomeLabel.grid(column=1, row=0, pady=20, padx=100)
    opMenu=tk.OptionMenu(root,muscleGroup,  'Chest', 'Back', 'Legs', 'Arms', 'Cardio', 'Core/Abs', "Shoulders")
    opMenu.grid(column=1, row=1, pady=10)
    
    return [opMenu]

if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()