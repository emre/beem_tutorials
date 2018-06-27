from beem.account import Account


def main():
    acc = Account("emrebeyler")
    print(acc.get_expiring_vesting_delegations())


if __name__ == '__main__':
    main()
