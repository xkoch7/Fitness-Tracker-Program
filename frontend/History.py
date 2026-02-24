import json

def cycleEntries(step):
    from vars import index, widgets
    if step == 1:
        index += 3
    elif step == -1:
        index -= 3
    
    from vars import email
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        workouts = data['workoutData'].get(email, [])
    
        if workouts== []:
            noWorkouts=tk.Label(root, text="No workouts logged yet.", font=("Helvetica", 20),fg="red")
            noWorkouts.grid(row=7, column=1)
            root.after(2000, lambda: noWorkouts.grid_forget())
            return
        else:
            workout1 = workouts[index%len(workouts)]    
            workout2 = workouts[(index+1)%len(workouts)]
            workout3 = workouts[(index+2)%len(workouts)]
            workoutInfo3=f"Muscle Group: {workout3[0]}, Workout: {workout3[1]}, Reps: {workout3[2]}, Sets: {workout3[3]}, Weight: {workout3[4]}"
            workoutInfo2=f"Muscle Group: {workout2[0]}, Workout: {workout2[1]}, Reps: {workout2[2]}, Sets: {workout2[3]}, Weight: {workout2[4]}"
            workoutInfo1=f"Muscle Group: {workout1[0]}, Workout: {workout1[1]}, Reps: {workout1[2]}, Sets: {workout1[3]}, Weight: {workout1[4]}"
            workoutLabel3=tk.Label(root, text=workoutInfo3, font=("Helvetica", 15),wraplength=500,justify="center")
            workoutLabel2=tk.Label(root, text=workoutInfo2, font=("Helvetica", 15),wraplength=500,justify="center")
            workoutLabel1=tk.Label(root, text=workoutInfo1, font=("Helvetica", 15),wraplength=500,justify="center")
            if len(workouts) >= 3:
                workoutLabel1.grid(row=7, column=1)
                workoutLabel2.grid(row=8, column=1)
                workoutLabel3.grid(row=9, column=1)
                if workoutLabel1 not in widgets:
                    widgets.append(workoutLabel1)
                    widgets.append(workoutLabel2)
                    widgets.append(workoutLabel3)
            elif len(workouts) == 2:
                workoutLabel1.grid(row=7, column=1)
                workoutLabel2.grid(row=8, column=1)
                if workoutLabel1 not in widgets:
                    widgets.append(workoutLabel1)
                    widgets.append(workoutLabel2)
            elif len(workouts) == 1:
                workoutLabel1.grid(row=7, column=1)
                if workoutLabel1 not in widgets:
                    widgets.append(workoutLabel1)
    

def setup(root,tk) -> list:
    cycleEntries(0)
    historyLabel=tk.Label(root, text="Workout History", font=("Helvetica", 16))
    historyLabel.grid(column=1, row=0, pady=20, padx=100)
    nextBtn = tk.Button(root, text="Next", width=20, height=2, command=lambda: cycleEntries(1))
    nextBtn.grid(column=1, row=2, pady=10,padx=100)
    prevBtn = tk.Button(root, text="Previous", width=20, height=2, command=lambda: cycleEntries(-1))
    prevBtn.grid(column=1, row=3, pady=10,padx=100)
    return [historyLabel, nextBtn, prevBtn]
    

if __name__ == "__main__":
    import os
    import sys
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.append(PROJECT_ROOT)
    import tkinter as tk
    root= tk.Tk()
    #setting title and page size
    root.title("T&X Fitness")
    root.geometry("500x850")
    setup(root,tk)
    root.mainloop()