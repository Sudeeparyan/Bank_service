from typing import Optional, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import json, os
import uvicorn

# bank_accounts dict to save the account details
# This dict will be dumped to the json file (which acts like a database)
bank_accounts = {}

class Payee(BaseModel):
    id: str
    name: str
    nickname: str
    account_id: str
    ifsc_code: str

class Account(BaseModel):
    id: str
    first_name: str
    last_name: str
    date_of_birth: str
    Address: str
    Nationality: str
    fathers_name: str
    mothers_name: str
    aadhar_id: str
    pan_id: str
    balance: float
    payee_list: Optional[Dict[str, Payee]] = {}

# FastAPI app instance
app = FastAPI()

def get_json_path():
    json_path = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(json_path, "bank_accounts.json")
    return json_path

def read_account_log():
    """
    To load the initial set of accounts from the json file (which acts as a database)
    """
    
    with open(get_json_path(), 'r') as account_log:
        global bank_accounts
        bank_accounts = json.load(account_log)

read_account_log()
def write_account_log():
    """
    To write the changes to the json file (database)
    """
    with open(get_json_path(), 'w') as account_log:
        global bank_accounts
        json.dump(bank_accounts, account_log, sort_keys=True, indent=4)

@app.get("/v1/home")
async def home():
    return {"message": "Welcome to bank service"}

if __name__ == "__main__":
    # Serve the app with uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000 )
