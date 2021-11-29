import requests


def handle_cur():
    cur_choice = input(
        """Options: \n\t Show all Currencies:       --> Type: show all cur
                \n\t Show Currency              --> Type: show "name"
                \n\t Add Currency               --> Type: add "name" 
                \n\t Delete Currency            --> Type: del "name" 
                \n\t Change Price               --> Type: change "name" 
                \n\t BAD AUTH                   --> Type: bad boy \nType: """
    )

    if cur_choice.lower() == "show all cur":
        show_all()
    elif cur_choice.split()[0].lower() == "show":
        show_cur(cur_choice.split()[1])
    elif cur_choice.split()[0].lower() == "add":
        add_cur(cur_choice.split()[1])
    elif cur_choice.split()[0].lower() == "del":
        del_cur(cur_choice.split()[1])
    elif cur_choice.split()[0].lower() == "change":
        change_cur(cur_choice.split()[1])
    elif cur_choice.split()[0].lower() == "bad":
        show_all_bad()
    else:
        print("WTF")


def show_all():
    response = requests.get(
        "https://localhost:5001/api/price/all",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
    )
    print(f"ALL PRICES: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")


def show_all_bad():
    response = requests.get(
        "https://localhost:5001/api/price/all",
        headers={"ApiKey": "WRONG API KEY"},
        verify=False,
    )
    print(f"ALL PRICES: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")


def show_cur(cur):
    response = requests.get(
        f"https://localhost:5001/api/price/{cur.lower()}",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
    )
    print(f"Stats: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")


def add_cur(cur):
    cur_name = cur.lower()
    cur_price = int(input("\nPlease enter the current price of the Currency: "))
    response = requests.post(
        f"https://localhost:5001/api/price/",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
        json={"name": cur_name, "value": cur_price},
    )
    show_all()
    print(f"STATUS CODE: {response.status_code}")


def del_cur(cur):
    response = requests.delete(
        f"https://localhost:5001/api/price/{cur.lower()}",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
    )
    print(f"Stats: \n{response.text}")
    print(f"STATUS CODE: {response.status_code}")


def change_cur(cur):
    cur_name = cur.lower()
    new_price = int(input("\nPlease enter the NEW price of the Currency: "))
    response = requests.put(
        f"https://localhost:5001/api/price/",
        headers={"ApiKey": "ich-bin-ein-super-sicherer-api-key"},
        verify=False,
        json={"name": cur_name, "value": new_price},
    )
    show_all()
    print(f"STATUS CODE: {response.status_code}")
