import argparse
from bitshares.account import Account
from bitshares.exceptions import AccountDoesNotExistsException

user = argparse.ArgumentParser()
user.add_argument("-u", "--user", required=True, help="bitshare username")
args = vars(user.parse_args())

try:
    account = Account("{}" .format(args["user"]))
    for balance in account.balances:
        print(balance, "\n")
except AccountDoesNotExistsException:
    print("The user you're looking for does not exist.")
