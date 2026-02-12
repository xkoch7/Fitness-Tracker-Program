
import json
DATAFILE = 'Backend\\UserInfo.json'
def getInfo(emailVar, passVar) -> bool:
    #opening data file in order to check if email and password entered are saved
    #used in login_UI.py when user is logging in
    with open(DATAFILE,"r", encoding="utf-8") as f:
        emails= json.load(f)['emails']
        if emailVar not in emails.keys():
            
            return False
        else:
            if emails[emailVar]!=passVar:
                #return error wrong password
                return False
            
            return True
        
            
    
#function to allow user to create account and writes information to json file

def createAcc(emailVar, passVar):
    with open(DATAFILE,"r" ) as f:
        emails= json.load(f)
        emails['emails'][emailVar] = passVar
        emails['workoutData'][emailVar] = {}
    
    with open(DATAFILE,"w", encoding="utf-8") as f:
        json.dump(emails, f, indent=4)
        

def createAcc(email_var, pass_var):
    with open(DATA_FILE,"W", encoding="utf-8") as f:
        emails= json.load(f)['emails']
        emails[email_var] = pass_var


        json.dump({"emails": emails}, f, indent=4)
if __name__ == "__main__":
    import tkinter as tk
    root= tk.Tk()
    em=tk.StringVar(value="test1")
    pw=tk.StringVar(value="test2")
    createAcc(em.get(), pw.get())
