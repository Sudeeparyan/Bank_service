import dash
from dash import Dash, html, callback, ctx
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import os
import requests


os.chdir(os.path.dirname(__file__))
backend_url = "http://localhost:8000"

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

create_account_layout = dbc.Row(
    [
        dbc.Col(),
        dbc.Col(
            children=[
                dbc.Card(
                    [
                        dbc.CardHeader("Enter Details"),
                        dbc.CardBody(
                            [
                                dbc.Label("Enter Account ID"),
                                dbc.Input(
                                    id=("account_id"),
                                    placeholder="Enter Unique Account ID",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("First Name"),
                                dbc.Input(
                                    id=("first_name"),
                                    placeholder="Enter First Name",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Last Name"),
                                dbc.Input(
                                    id=("last_name"),
                                    placeholder="Enter Last Name",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Date of Birth"),
                                dbc.Input(
                                    id=("date_of_birth"),
                                    placeholder="Enter Date of Birth",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Address"),
                                dbc.Input(
                                    id=("address"),
                                    placeholder="Enter Address",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Fathers Name"),
                                dbc.Input(
                                    id=("fathers_name"),
                                    placeholder="Enter Fathers Name",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Mothers Name"),
                                dbc.Input(
                                    id=("mothers_name"),
                                    placeholder="Enter Mothers Name",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Aadhar Number"),
                                dbc.Input(
                                    id=("aadhar_id"),
                                    placeholder="Enter Aadhar Number",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Pan Id"),
                                dbc.Input(
                                    id=("pan_id"),
                                    placeholder="Enter Pan Id",
                                    type="text",
                                    value="",
                                ),
                                dbc.Label("Nationality"),
                                dbc.Input(
                                    id=("nationality"),
                                    placeholder="Enter Nationality",
                                    type="text",
                                    value="",
                                ),
                                dbc.Button(
                                    "Create Account",
                                    id="create_account_button",
                                    className="margin-top",
                                ),
                                dbc.Label(
                                    "*Note: Enter all the details",
                                    id="create_warning_message",
                                    hidden=True,
                                    color="red"
                                ),
                            ],
                        ),
                    ],
                )
            ],
        ),
        dbc.Col()
    ]
)
    

account_details_layout = dbc.Card(
    [
        dbc.CardHeader("Account Details"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(dbc.Label("Account Number"),width=3),
                        dbc.Col(
                            dbc.Input(
                                id=("account_number"),
                                placeholder="Enter Account Number",
                                type="text",
                                value="",
                            ),width=4
                        )
                    ],
                    className="margin-top",
                ),
                dbc.Row(
                    [
                        dbc.Col(dbc.Label("Enter Amount to Withdraw"),width=3),
                        dbc.Col(
                            dbc.Input(
                                id=("withdraw_amount"),
                                placeholder="Enter Amount to Withdraw",
                                type="text",
                                value="",
                            ),width=4
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Withdraw",
                                id="withdraw_amount_button",
                            ),width=3
                        ),
                        dbc.Toast(
                            [
                                html.P(
                                    children=[""],
                                    id="withdraw_toast_message",
                                )
                            ],
                            id="withdraw_auto_toast",
                            duration=4000,
                            is_open=False,
                            style={
                                "position": "fixed",
                                "top": 30,
                                "right": 20,
                                "width": "fit-content",
                            },
                        ),
                    ],className="margin-top",
                ),
                dbc.Row(
                    [
                        dbc.Col(dbc.Label("Enter Amount to Deposit"),width=3),
                        dbc.Col(
                            dbc.Input(
                                id=("deposit_amount"),
                                placeholder="Enter Amount to Deposit",
                                type="text",
                                value="",
                            ),width=4
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Deposit",
                                id="deposit_amount_button",
                            ),width=3
                        ),
                        dbc.Toast(
                            [
                                html.P(
                                    children=[""],
                                    id="deposit_toast_message",
                                )
                            ],
                            id="deposit_auto_toast",
                            duration=4000,
                            is_open=False,
                            style={
                                "position": "fixed",
                                "top": 30,
                                "right": 20,
                                "width": "fit-content",
                            },
                        ),
                    ],className="margin-top",
                ),
                dbc.Row(
                    [                   
                        dbc.Col(
                            dbc.Button(
                                "Check Balance",
                                id="check_balance_button",
                            ),width=3
                        ),
                        dbc.Col(
                            dbc.Input(
                                id=("account_balance"),
                                type="text",
                                value="",
                            ),width=4
                        ),
                        dbc.Toast(
                            [
                                html.P(
                                    children=[""],
                                    id="balance_toast_message",
                                )
                            ],
                            id="balance_auto_toast",
                            duration=4000,
                            is_open=False,
                            style={
                                "position": "fixed",
                                "top": 30,
                                "right": 20,
                                "width": "fit-content",
                            },
                        ),
                    ],
                    className="margin-top",
                ),
            ]
        )
    ]
)


app.layout = html.Div([
    dbc.Tabs(
    [
        dbc.Tab(create_account_layout, label="Create Account"),
        dbc.Tab(account_details_layout, label="Account Details"),
    ]
)
])

# callback to trigger create account button click
@callback(
    #dummy output as of now
    output=dict(
        first_name_output=Output(
            "first_name", "style"
        ),
    ),
    inputs=dict(create_account_button=Input("create_account_button", "n_clicks")), #specify the id as first parameter in input and property as second parameter.
    state=dict(account_id = State("account_id", "value"),
                first_name=State("first_name", "value"),
                last_name=State("last_name", "value"),
                date_of_birth = State("date_of_birth", "value"),
                address = State("address", "value"),
                fathers_name = State("fathers_name", "value"),
                mothers_name=State("mothers_name", "value"),
                aadhar_id = State("aadhar_id", "value"),
                pan_id = State("pan_id", "value"),
                nationality = State("nationality", "value"),
               ), #can be used if need any data from the screen but not be an trigger to callback.
    prevent_initial_call=True,
)
def create_account_button_click(create_account_button,
    account_id,                             
    first_name,
    last_name,
    date_of_birth,
    address,
    fathers_name,
    mothers_name,
    aadhar_id,
    pan_id,
    nationality,
    ):
    # callback to trigger create account button click
    # Add functions
    account_details = {
        "Address": address,
        "Nationality": nationality,
        "aadhar_id": aadhar_id,
        "balance": 0,
        "date_of_birth": date_of_birth,
        "fathers_name": fathers_name,
        "first_name": first_name,
        "id": account_id,
        "last_name": last_name,
        "mothers_name": mothers_name,
        "pan_id": pan_id,
        "payee_list": {}
    }
    response = requests.post(backend_url+"/v1/account",json=account_details)
    raise PreventUpdate
    # hidden = True
    # if first_name:
    #     return dict(first_name_output="Output need to be specified",create_warning_message_output = hidden)
    # else:
    #     hidden = False
    #     return dict(first_name_output= dash.dash.no_update, create_warning_message_output = hidden )


# callback to trigger withdraw amount button click
# @callback(
#     #dummy output as of now
#     output=dict(
#         account_balance_output=Output(
#             "account_balance", "value"
#         ),
#         withdraw_toast_message_output=Output(
#             "withdraw_toast_message", "children"
#         ),
#         withdraw_toast_is_open_output=Output(
#             "withdraw_auto_toast", "is_open"
#         )
#     ),
#     inputs=dict(withdraw_amount_button=Input("withdraw_amount_button", "n_clicks")), #specify the id as first parameter in input and property as second parameter.
#     state=dict(withdraw_amount=State("withdraw_amount", "value"),
#                account_number=State("account_number", "value")), #can be used if need any data from the screen but not be an trigger to callback.
#     prevent_initial_call=True,
# )
# def withdraw_amount_button_click(withdraw_amount_button, withdraw_amount, account_number):
#     # callback to trigger withdraw button click
#     # Add functions
#     if withdraw_amount:
#         account_balance = requests.put((backend_url+"/v1/account/{0}/cash/withdraw?amount=10000").format(account_number)).json()["balance"]
#         return dict(account_balance_output=account_balance,withdraw_toast_message_output = dash.dash.no_update,withdraw_toast_is_open_output = dash.dash.no_update)
#     else:
#         return dict(account_balance_output= dash.dash.no_update, withdraw_toast_message_output = "Enter amount to withdraw", withdraw_toast_is_open_output = True)


# callback to trigger deposit amount button click
@callback(
    #dummy output as of now
    output=dict(
        # account_balance_output=Output(
        #     "account_balance", "value"
        # ),
        deposit_toast_message_output=Output(
            "deposit_toast_message", "children"
        ),
        deposit_toast_is_open_output=Output(
            "deposit_auto_toast", "is_open"
        )
    ),
    inputs=dict(deposit_amount_button=Input("deposit_amount_button", "n_clicks"),
                withdraw_amount_button=Input("withdraw_amount_button", "n_clicks")), #specify the id as first parameter in input and property as second parameter.
    state=dict(deposit_amount=State("deposit_amount", "value"),
               withdraw_amount=State("withdraw_amount", "value"),
               account_number=State("account_number", "value")), #can be used if need any data from the screen but not be an trigger to callback.
    prevent_initial_call=True,
)
def deposit_amount_button_click(deposit_amount_button, withdraw_amount_button, deposit_amount, withdraw_amount, account_number):
    # callback to trigger deposit amount button click
    # Add functions
    button_id = ctx.triggered_id
    if button_id == "deposit_amount_button":
        account_balance = requests.put((backend_url+"/v1/account/{0}/cash/deposit?amount=10000").format(account_number)).json()["balance"]
        return dict(deposit_toast_message_output = "Cash Deposit Successful",deposit_toast_is_open_output = dash.dash.no_update)
    if button_id == "withdraw_amount_button":
        account_balance = requests.put((backend_url+"/v1/account/{0}/cash/withdraw?amount=10000").format(account_number)).json()["balance"]
        return dict(withdraw_toast_message_output = "Cash Withdraw Successful",withdraw_toast_is_open_output = dash.dash.no_update)
    else:
        return dict(deposit_toast_message_output = "Enter amount to deposit", deposit_toast_is_open_output = True)

# callback to trigger check balance button click
@callback(
    #dummy output as of now
    output=dict(
        account_balance_output=Output(
            "account_balance", "value"
        ),
        balance_toast_message_output=Output(
            "balance_toast_message", "children"
        ),
        balance_toast_is_open_output=Output(
            "balance_auto_toast", "is_open"
        )
    ),
    inputs=dict(check_balance_button=Input("check_balance_button", "n_clicks")), #specify the id as first parameter in input and property as second parameter.
    state=dict(account_number=State("account_number", "value")), #can be used if need any data from the screen but not be an trigger to callback.
    prevent_initial_call=True,
)
def check_balance_button_click(check_balance_button, account_number):
    # callback to trigger check balance button click
    # Add functions
    if account_number:
        account_balance = requests.get((backend_url+"/v1/account/{0}/balance").format(account_number)).json()["balance"]
        return dict(account_balance_output=account_balance,balance_toast_message_output = dash.dash.no_update,balance_toast_is_open_output = dash.dash.no_update)
    else:
        return dict(account_balance_output= dash.dash.no_update, balance_toast_message_output = "Enter account number", balance_toast_is_open_output = True)



if __name__ == '__main__':
    app.run_server(debug=True, port=8066)