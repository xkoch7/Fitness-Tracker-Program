import sys
import os
import threading
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
import vars
# import frontend.login_UI as login_UI
import frontend.HomeScreen as HomeScreen
import frontend.login_UI as login_UI
screens = [0, login_UI, HomeScreen]
while vars.screen < len(screens) and vars.screen >= 0:
    vars.widgets = screens[vars.screen].setup(vars.root, vars.tk)
    if vars.screen == 0:
        break
    vars.root.mainloop()
        