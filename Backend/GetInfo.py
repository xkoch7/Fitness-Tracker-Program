
import json
DATA_FILE = 'UserInfo.json'
def getInfo(email_var, pass_var):
    with open(DATA_FILE,"r", encoding="uft-8"):
        emails= json.load(DATA_FILE)
        if not emails[email_var]:
             #return error email not registered
             pass
        elif emails[email_var]== pass_var:
            #log them in
            pass
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)