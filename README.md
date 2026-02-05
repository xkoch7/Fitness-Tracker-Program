

## Fitness-Tracker-Program

# Overview

Using python and tkinter we plan on making a fitness tracker program. With a clean UI login capabilites along with knowledge on fitness and exercise workouts. We both enjoy working out at not just the school gym but at home and at a boxing gym. We are passionate about this project because we did not have muhc guidance when beggining our own fitness journey and want to help others. We both think fitness is an important aspect in anyone life no matter their skill level.

This app will allow the user to add workouts to their personal database to allow for easier tracking of their progress of the gym. Its perfect for those who want to take their fitness journey to the next level and really get into keeping themselves healthy.

# Build and Run Instructions

**Requirements:**
 - Python 3.6+ (with tkinter, pillow  and json libraries)

# Structure/Design
**Structure:**
```
Fitness-Tracker-Program/
├── main.py                # Entry point
├── vars.py                # global varibles 
├── Backend/
│   ├── UserInfo.json      # Json file for user data
│   └── getInfo.py         # Login Logic
└── frontend/
    ├── Images/
        └── ...
    ├── login_UI.py        # UI Frame 1
    └── HomeScreen.py      # UI Frame 2
```

**Design:**

Exectuing main will start the user from the login screen and from there the entire app is availible. For testing or indiviual viewing each file can be run independently of each other. Global variables are kept in a seperate vars file so that each screen and the main file can access them and can edit them during runtime.

# Current Limitaitons

- Settings, Track Workout and View History are under development

- Login and Signup are not fully fleshed out and are only functional for testing

# Git to Run
In bash run:
 ``` bash
 git clone https://github.com/xkoch7/Fitness-Tracker-Program.git

 cd Fitness-Tracker-Program
 ```

Then in terminal run:

    pip install -r requirements.txt
    
Finally run:

    python -m main