from time import sleep
import requests
from cur_handler import handle_cur
from acc_handler import handle_acc
import urllib3
from tqdm import tqdm


urllib3.disable_warnings()


def main():
    # for i in tqdm(range(100), desc="Heavy Connection work..."):
    #    sleep(0.05)
    decision()


def decision():
    user_decision = input(
        "Type: cur for Currencies or acc for Accounts for further options: "
    )
    while user_decision != "exit":
        if user_decision.lower() == "cur":
            handle_cur()
        elif user_decision.lower() == "acc":
            handle_acc()
        else:
            print("WTF")
        user_decision = input(
            "Type: cur for Currencies or acc for Accounts for further options: "
        )


if __name__ == "__main__":
    main()
