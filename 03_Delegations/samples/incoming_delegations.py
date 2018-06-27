from beem.account import Account


def main():
    acc = Account('emrebeyler')
    for operation in acc.history(only_ops=["delegate_vesting_shares",]):
        print("Delegation from @%s to @%s, %s, at %s" % (
            operation["delegator"],
            operation["delegatee"],
            operation["vesting_shares"],
            operation["timestamp"])
        )


if __name__ == '__main__':
    main()
