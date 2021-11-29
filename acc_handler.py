import requests
import json


def handle_acc():
    cur_choice = input(
        """Options: \n\t Show all Accounts:       --> Type: show all acc
                \n\t Show Account stats:          --> Type: show "name"
                \n\t Add Account:                 --> Type: add "name" 
                \n\t Delete Account:              --> Type: del "name" \nType: """
    )

    if cur_choice.lower() == "show all acc":
        show_all()
    elif cur_choice.split()[0].lower() == "show":
        show_acc(cur_choice.split()[1])
    elif cur_choice.split()[0].lower() == "add":
        add_acc(cur_choice.split()[1])
    elif cur_choice.split()[0].lower() == "del":
        del_acc(cur_choice.split()[1])
    else:
        print("WTF")


def show_all():
    response = requests.get(
        "https://localhost:5001/api/account/all",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
    )
    print(f"ALL Accounts: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")


def show_acc(cur):
    response = requests.get(
        f"https://localhost:5001/api/account/{cur}",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
    )
    print(f"Stats: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")


# //{
# //    "name": "Ben Dover",
# //    "currencyName": "IOTA",
# //    "amount": 2222
# //}
def add_acc(cur):
    acc_name = cur.lower()
    acc_cur_name = input("\nPlease enter the currencie name the Account is holding: ")
    acc_cur_amount = int(input("\nPlease enter the amount the Account is holding: "))
    data = {"name": acc_name, "currencyName": acc_cur_name, "amount": acc_cur_amount}
    dummy = {"name": "TITO", "currencyName": "EXYU", "amount": 42}
    print(json.dumps(data, indent=4))
    response = requests.post(
        f"https://localhost:5001/api/account/",
        verify=False,
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        json=data,
    )
    show_all()
    print(f"STATUS CODE: {response.status_code}")


def del_acc(cur):
    response = requests.delete(
        f"https://localhost:5001/api/account/{cur.lower()}",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
    )
    print(f"Stats: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")
