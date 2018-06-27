<img src="https://steemitimages.com/0x0/https://cdn.utopian.io/posts/d563a408c062506aed88befbe7781399184fbeem-logo.png">

#### Repository of Beem
[https://github.com/holgern/beem](https://github.com/holgern/beem)    

#### Tutorial Content

You will learn how to:

- Create/Revoke delegations 
- See incoming/outgoing delegations for a particular account
- See expiring outgoing delegations

with using Beem.

#### Requirements

- Python 2.7.x or 3.4+
- Basic Python knowledge
- Beem

***

#### Delegations

With the Hard Fork 18, STEEM blockchain gained a new mechanic where accounts can delegate their STEEM POWER to other accounts. It's been widely used in the network that:

- You can delegate your SP to bidbots and earn passive income
- You can support curator teams or decentralized apps (Utopian, Dlive, Dtube, etc) by delegating some of your stake.

It has some limitations, though. 

- Delegated SP cannot be powered down.
- It takes 1 week to get your SP back after revoking delegation.

#### Creating delegations with Beem

The Account class located at ```beem.account``` has a create_vesting_delegations function exactly does that.

It receives 2 positional, 1 keyword argument.

| Parameter      | Value                                                                | Required |
|----------------|----------------------------------------------------------------------|----------|
| to_account     | The account we delegate to                                           | True     |
| vesting_shares | The amount of vests we will delegate.                                | True     |
| account        | The account we delegate from. If not given, default account is used. | False    |

Example:

```python
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

```

This scripts delegates 1 SP to @holger80.

<img src="https://steemitimages.com/0x0/https://cdn.steemitimages.com/DQmbnRe8SAcbNHeNohkEuuktzeCJ7sw2oX59rRTnruY83to/Screen%20Shot%202018-06-27%20at%209.45.45%20PM.png">
<sup><center>steemd represantation of the post</center></sup>

**Note**: The amount of SP to delegate is passed as [VESTS](https://www.steem.center/index.php?title=Vest). We use Beem's convertion helpers (```steem.sp_to_vests(<amount>)``` to pass the amount in VESTS form.)

#### Creating delegations with Beem

It has the same mechanics except one little change. This time we will pass the amount as zero.

```python
...
resp = acc.delegate_vesting_shares(
    "holger80",
    s.sp_to_vests(0),
    account="emrebeyler"
)
...
```

#### Getting expiring delegations

When you revoke your delegation, there is a one week cooldown period to get the SP back in use. If you delegate/undelegate multiple times, you get confused when you get your SP back.

Steem daemon has a call that answers that questions. 

```python
from beem.account import Account

acc = Account("emrebeyler")
print(acc.get_expiring_vesting_delegations())
```

Which results in a format like this:

```
[{
    'id': 2383746,
    'delegator': 'emrebeyler',
    'vesting_shares': '1524880.277777 VESTS',
    'expiration': '2018-06-29T13:54:39'
}, {
    'id': 2425799,
    'delegator': 'emrebeyler',
    'vesting_shares': '2030.376597 VESTS',
    'expiration': '2018-07-04T18:49:51'
}]
```

#### Incoming Delegations

If you want to find out the delegators of an account, there is no call for that. So we will parse the account's history on the network and filter the related operations to gain that information.

```python
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


```

We will go into more details with **history** function in upcoming tutorials. It's a function where you can get all operations related to a particular account. We pass ```only_ops``` parameter as ```delegate_vesting_shares``` since we're only interested in delegation operations for this script.

**Note:** You may need to implement a simple state machine to learn which delegations are active or expired. If a delegation operation created with 0 VESTS, that means the previous delegation from that account is not active any more.


#### Outgoing Delegations

Luckily, steem daemon has a call for that. Let's see which projects are supported by Steemit INC. :)

```python
from beem.account import Account


def main():
    acc = Account('misterdelegations')
    print(acc.get_vesting_delegations())


if __name__ == '__main__':
    main()
```

Output:

```
[{
    'id': 628632,
    'delegator': 'misterdelegation',
    'delegatee': 'binance-hot',
    'vesting_shares': '2045385.892695 VESTS',
    'min_delegation_time': '2018-02-07T03:26:12'
}, {
    'id': 875709,
    'delegator': 'misterdelegation',
    'delegatee': 'bittrex',
    'vesting_shares': '20368452.908257 VESTS',
    'min_delegation_time': '2018-04-27T20:23:36'
}, {
    'id': 498415,
    'delegator': 'misterdelegation',
    'delegatee': 'busy.pay',
    'vesting_shares': '1023794071.582442 VESTS',
    'min_delegation_time': '2018-01-16T19:22:42'
}, {
    'id': 481299,
    'delegator': 'misterdelegation',
    'delegatee': 'dlive',
    'vesting_shares': '4196010718.000000 VESTS',
    'min_delegation_time': '2018-01-09T19:55:33'
}, {
    'id': 481300,
    'delegator': 'misterdelegation',
    'delegatee': 'dsound',
    'vesting_shares': '2012045501.000000 VESTS',
    'min_delegation_time': '2018-01-09T19:56:06'
}, {
    'id': 628666,
    'delegator': 'misterdelegation',
    'delegatee': 'dtube',
    'vesting_shares': '4090769551.344561 VESTS',
    'min_delegation_time': '2018-02-07T03:41:24'
}, {
    'id': 628621,
    'delegator': 'misterdelegation',
    'delegatee': 'esteemapp',
    'vesting_shares': '1022693158.741604 VESTS',
    'min_delegation_time': '2018-02-07T03:20:48'
}, {
    'id': 959966,
    'delegator': 'misterdelegation',
    'delegatee': 'fundition',
    'vesting_shares': '2031960454.534957 VESTS',
    'min_delegation_time': '2018-06-12T23:36:18'
}, {
    'id': 628656,
    'delegator': 'misterdelegation',
    'delegatee': 'mack-bot',
    'vesting_shares': '515745189.000000 VESTS',
    'min_delegation_time': '2018-02-07T03:36:39'
}, {
    'id': 875710,
    'delegator': 'misterdelegation',
    'delegatee': 'poloniex',
    'vesting_shares': '20368452.651172 VESTS',
    'min_delegation_time': '2018-04-27T20:23:51'
}, {
    'id': 265479,
    'delegator': 'misterdelegation',
    'delegatee': 'sndbox',
    'vesting_shares': '304973163.465792 VESTS',
    'min_delegation_time': '2017-09-25T21:34:54'
}, {
    'id': 498411,
    'delegator': 'misterdelegation',
    'delegatee': 'spaminator',
    'vesting_shares': '5457084334.000000 VESTS',
    'min_delegation_time': '2018-01-16T19:19:45'
}, {
    'id': 628700,
    'delegator': 'misterdelegation',
    'delegatee': 'steemcleaners',
    'vesting_shares': '3068075031.813693 VESTS',
    'min_delegation_time': '2018-02-07T04:00:48'
}, {
    'id': 940346,
    'delegator': 'misterdelegation',
    'delegatee': 'steemhunt',
    'vesting_shares': '2033154493.315696 VESTS',
    'min_delegation_time': '2018-06-01T17:45:03'
}, {
    'id': 940348,
    'delegator': 'misterdelegation',
    'delegatee': 'steemit-jp',
    'vesting_shares': '508288596.538036 VESTS',
    'min_delegation_time': '2018-06-01T17:46:12'
}, {
    'id': 940345,
    'delegator': 'misterdelegation',
    'delegatee': 'steempress-io',
    'vesting_shares': '2033154545.053620 VESTS',
    'min_delegation_time': '2018-06-01T17:44:00'
}, {
    'id': 959967,
    'delegator': 'misterdelegation',
    'delegatee': 'tasteem',
    'vesting_shares': '2031960380.365700 VESTS',
    'min_delegation_time': '2018-06-12T23:37:03'
}, {
    'id': 361062,
    'delegator': 'misterdelegation',
    'delegatee': 'trendings-grace',
    'vesting_shares': '697229371.000000 VESTS',
    'min_delegation_time': '2017-12-04T22:32:09'
}, {
    'id': 314685,
    'delegator': 'misterdelegation',
    'delegatee': 'utopian-io',
    'vesting_shares': '2083312462.000000 VESTS',
    'min_delegation_time': '2017-11-07T13:43:54'
}]
```

#### Curriculum

- [Introduction to Beem and creating a post with it](/@emrebeyler/beem-tutorials-1-introduction-to-beem-and-creating-a-post-with-it)
- [Setting beneficiaries with Beem](/@emrebeyler-beem-tutorials-2-setting-beneficiaries=with-beem)
- [Delegations with Beem](@emrebeyler-beem-tutorials-3-delegations-with-beem)

#### Sample Codes

[Samples](https://github.com/emre/beem_tutorials/tree/master/03_Delegations/samples)

