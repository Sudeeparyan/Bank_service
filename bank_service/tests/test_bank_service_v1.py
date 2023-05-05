import json
import pytest
import requests


account_id = "100"


@pytest.mark.create
def test_create_account(root_url):
    """Tests the end point for creating a new account"""

    new_account_details = {
        "Address": "Coimbatore",
        "Nationality": "Indian",
        "aadhar_id": "11223344",
        "balance": 10000.0,
        "date_of_birth": "16 Feb 1994",
        "fathers_name": "test",
        "first_name": "User1",
        "id": account_id,
        "last_name": "lastname1",
        "mothers_name": "test",
        "pan_id": "123L",
        "payee_list": {}
    }
    new_account_details_str = json.dumps(new_account_details)

    response = requests.post(root_url + "/v1/account", data=new_account_details_str)
    assert response.status_code == 200
    assert response.json() == {
        "id": account_id,
        "first_name": "User1",
        "last_name": "lastname1",
        "date_of_birth": "16 Feb 1994",
        "Address": "Coimbatore",
        "Nationality": "Indian",
        "fathers_name": "test",
        "mothers_name": "test",
        "aadhar_id": "11223344",
        "pan_id": "123L",
        "balance": 10000.0,
        "payee_list": {}
    }


@pytest.mark.amount
@pytest.mark.parametrize("amount", [10000, 20000, 30000])
def test_deposit(root_url, amount):
    """Tests the end point for depositing an amount into the account"""

    response = requests.get(root_url + f"/v1/account/{account_id}/balance")
    assert response.status_code == 200
    balance = response.json()["balance"]

    response = requests.put(root_url + f"/v1/account/{account_id}/cash/deposit?amount={amount}")
    assert response.status_code == 200
    assert response.json()["balance"] == balance + amount


@pytest.mark.amount
def test_withdraw(root_url):
    """Tests the end point for withdrawing an amount into the account"""

    response = requests.get(root_url + f"/v1/account/{account_id}/balance")
    assert response.status_code == 200
    balance = response.json()["balance"]

    response = requests.put(root_url + f"/v1/account/{account_id}/cash/withdraw?amount=10000")
    assert response.status_code == 200
    assert response.json()["balance"] == balance - 10000
