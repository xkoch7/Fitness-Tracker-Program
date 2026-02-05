
import json
DATA_FILE = 'Backend\\UserInfo.json'
def getInfo(email_var, pass_var) -> bool:
    #opening data file in order to check if email and password entered are saved
    #used in login_UI.py when user is logging in
    with open(DATA_FILE,"r", encoding="utf-8") as f:
        emails= json.load(f)['emails']
        if email_var not in emails.keys():
            
            return False
        else:
            if emails[email_var]!=pass_var:
                #return error wrong password
                return False
            
            return True
        
            
    
    with open(f, 'w') as f:
        json.dump(f, indent=4)
#function to allow user to create account and writes information to json file
def createAcc(email_var, pass_var):
    with open(DATA_FILE,"W", encoding="utf-8") as f:
        emails= json.load(f)['emails']
        emails[email_var] = pass_var

    with open(f, 'w') as f:
        json.dump(f, indent=4)
if __name__ == "__main__":
    import os
    print(os.path.abspath(DATA_FILE))
