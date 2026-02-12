import threading
import time
import json
def verifyWorkout(workout):
    if workout[1] == 'Select Workout' and workout[2] == '0' and workout[3] == '0' and workout[4] == '0':
        return False
    return True
def addWorkout(root, tk,workout):
    import vars
    # verify inputs
    if not verifyWorkout(workout):
        fillOutText=tk.Label(root, text="Please fill out all workout fields.", font=("Helvetica", 10),fg="red")
        fillOutText.grid(row=7, column=1)
        root.after(2000, lambda: fillOutText.grid_forget())
        return False
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        data['workoutData'][vars.email].append(workout)
    
    with open('Backend\\UserInfo.json', 'w') as f:
        json.dump(data, f, indent=4)

def updateWorkoutList(root, tk, muscleGroupValue):
    workoutStats=[]
    workout=tk.StringVar(value='Select Workout')
    reps= tk.StringVar(value='0')
    sets= tk.StringVar(value='0')
    weight= tk.StringVar(value='0')
    while True:
        
        addWorkoutBtn = tk.Button(root, text="Add Workout", width=20, height=2,command=lambda: addWorkout(root,tk,workoutStats))
        subOpMenu=tk.OptionMenu(root,workout, 'Select Workout',[])
        repsEntry=tk.Entry(root, textvariable = reps, font=("calibre", 10,"normal"))
        setsEntry=tk.Entry(root, textvariable = sets, font=("calibre", 10,"normal"))
        weightEntry=tk.Entry(root, textvariable = weight, font=("calibre", 10,"normal"))

        while muscleGroupValue.get() != "Select Group":
            
            workoutOptions = {
                'Chest': ['Bench Press', 'Incline Dumbbell Press', 'Chest Fly'],
                'Back': ['Pull-ups', 'Deadlifts', 'Bent-over Rows'],
                'Legs': ['Squats', 'Lunges', 'Leg Press'],
                'Arms': ['Bicep Curls', 'Tricep Dips', 'Hammer Curls']
            }
            if muscleGroupValue.get() == "Other":
                otherLabel=tk.Label(root, text="Please enter workout name:", font=("calibre", 10,"normal"))
                otherWorkout=tk.StringVar(value='0')
                otherEntry=tk.Entry(root, textvariable = otherWorkout, font=("calibre", 10,"normal"))
                otherEntry.grid(column=1, row=2,padx=100, pady=10)
                otherLabel.grid(column=0, row=2, padx=100, pady=10)
                workoutStats=[muscleGroupValue.get(), otherWorkout.get(), reps.get(), sets.get(), weight.get()]
            else:
                otherEntry.grid_forget()
                otherLabel.grid_forget()
                
            workoutStats=[muscleGroupValue.get(), workout.get(), reps.get(), sets.get(), weight.get()]
            specWorkouts = workoutOptions.get(muscleGroupValue.get(), [])
            subOpMenu=tk.OptionMenu(root,workout,'Select Workout',*specWorkouts)
            addWorkoutBtn.grid(column=1, row=2,padx=100, pady=10)
            subOpMenu.grid(column=1, row=3,padx=100, pady=10)    
            tk.Label(root, text = "Reps:", font=("calibre", 10,"normal")).grid(column=0, row=4, padx =100, pady = 10)
            repsEntry.grid(column=1, row=4,padx=100, pady=10)    
            tk.Label(root, text = "Sets:", font=("calibre", 10,"normal")).grid(column=0, row=5, padx =100, pady = 10)
            setsEntry.grid(column=1, row=5,padx=100, pady=10) 
            tk.Label(root, text = "Weight:", font=("calibre", 10,"normal")).grid(column=0, row=6, padx =100, pady = 10)
            weightEntry.grid(column=1, row=6,padx=100, pady=10) 
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
    opMenu=tk.OptionMenu(root,muscleGroup,  'Chest', 'Back', 'Legs', 'Arms', 'Cardio', 'Core/Abs', "Shoulders", "Other")
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