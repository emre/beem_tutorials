from beem.account import Account


def main():
    acc = Account('misterdelegation')
    print(acc.get_vesting_delegations())


if __name__ == '__main__':
    main()
