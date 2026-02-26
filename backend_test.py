from Backend import GetInfo
from frontend import TrackWorkout
import json, vars
def test_login():
    import tkinter as tk
    root= tk.Tk()
    root.title("T&X Fitness")
    root.geometry("500x850")
    # Test creating an account (Pass)
    em=tk.StringVar(value="test1")
    pw=tk.StringVar(value="test2")
    GetInfo.createAcc(em.get(), pw.get())
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        assert em.get() in data['emails']
        assert data['emails'][em.get()] == pw.get()
       
    pw=tk.StringVar(value="")
    # Test creating an account with empty password (Fail)
    assert not GetInfo.createAcc(em.get(), pw.get())
    
    # Test creating an account with empty email (Fail)
    em=tk.StringVar(value="")
    pw=tk.StringVar(value="test2")
    assert not GetInfo.createAcc(em.get(), pw.get())
    
    # Test email not found (Fail)
    em=tk.StringVar(value="nonexistent")
    pw=tk.StringVar(value="test2")
    assert not GetInfo.getInfo(em.get(), pw.get())
    
    # Test wrong password (Fail)
    em=tk.StringVar(value="test1")
    pw=tk.StringVar(value="wrongpassword")
    assert not GetInfo.getInfo(em.get(), pw.get())
    # Test correct login (Pass)
    em=tk.StringVar(value="test1")
    pw=tk.StringVar(value="test2")
    assert GetInfo.getInfo(em.get(), pw.get())
    
def test_workout_tracking():
    import tkinter as tk
    root= tk.Tk()
    root.title("T&X Fitness")
    root.geometry("500x850")
    # Test adding a workout (Pass)
    vars.email = "test1"
    workout = ["Chest", "Bench Press", 10, 3, 100]
    TrackWorkout.addWorkout(root, tk, workout)
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        assert workout in data['workoutData'][vars.email]
        
    # Test adding an invalid workout (Fail)
    workout = ["Chest", "Select Workout", 0, 0, 0]
    assert not TrackWorkout.verifyWorkout(workout)
    
    # Test adding two workouts and testing size  (Pass)
    workout = ["Arms", "Bicep Curls", 30, 4, 50]
    TrackWorkout.addWorkout(tk.Tk(), tk, workout)
    workout = ["Legs", "Squats", 20, 5, 150]
    TrackWorkout.addWorkout(tk.Tk(), tk, workout)
    with open('Backend\\UserInfo.json', 'r') as f:
        data = json.load(f)
        assert len(data['workoutData'][vars.email]) == 3
        del data['workoutData'][vars.email]
        del data['emails'][vars.email]
   