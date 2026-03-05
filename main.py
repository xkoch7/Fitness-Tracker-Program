import sys
import os
import threading
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
import vars
# import frontend.login_UI as login_UI
import frontend.HomeScreen as HomeScreen
import frontend.login_UI as login_UI
import frontend.createAccount as createAccount
import frontend.BMICalculator as BMICalculator
#setting different screens from other files
screens = [0, login_UI, HomeScreen, createAccount, BMICalculator]
#ensures that theres only one screen showing at a time
while vars.screen < len(screens) and vars.screen >= 0:
    vars.widgets = screens[vars.screen].setup(vars.root, vars.tk)
    if vars.screen == 0:
        break
    vars.root.mainloop()