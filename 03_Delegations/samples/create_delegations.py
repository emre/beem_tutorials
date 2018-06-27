from beem import Steem
from beem.account import Account


def main():
    s = Steem(
        keys=["<active_wif>"],
    )
    acc = Account('emrebeyler', steem_instance=s)
    resp = acc.delegate_vesting_shares(
        "holger80",
        s.sp_to_vests(1),
        account="emrebeyler"
    )

    print(resp)


if __name__ == '__main__':
    main()
