from bitshares.account import Account

account = Account("quintric-trust")

for balance in account.balances:
    print(balance, "\n")
