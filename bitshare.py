import argparse
from bitshares.account import Account

user = argparse.ArgumentParser()
user.add_argument("-u", "--user", required=True, help="bitshare username")
args = vars(user.parse_args())

account = Account("{}" .format(args["user"]))

for balance in account.balances:
    print("\n", balance, "\n")
