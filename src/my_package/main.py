import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
import my_package.vars as vars
import frontend.HomeScreen as HomeScreen
import frontend.loginUI as loginUI
import frontend.createAccount as createAccount
import frontend.TrackWorkout as TrackWorkout
import frontend.BMICalculator as BMIScreen
import frontend.History as HistoryScreen
#setting different screens from other files
screens = [0, loginUI, createAccount, HomeScreen, TrackWorkout, HistoryScreen, BMIScreen ]

def load_screen():
    
    if vars.screen < len(screens) and vars.screen >= 0:
        # Clear old widgets
        for widget in vars.widgets:
            widget.grid_forget()
        # Load new screen
        vars.root.grid_columnconfigure(0, weight=0)
        vars.root.grid_columnconfigure(2, weight=0)
        vars.widgets = screens[vars.screen].setup(vars.root, vars.tk)
        # Schedule next screen check
        
        
        vars.root.after(100, check_screen)

def check_screen():
    if vars.screen < len(screens) and vars.screen >= 0:
        if vars.screen != vars.current_screen:
            vars.current_screen = vars.screen
            load_screen()
    vars.root.after(100, check_screen)

# Initialize and start the app
vars.current_screen = vars.screen
load_screen()
check_screen()
vars.root.mainloop()