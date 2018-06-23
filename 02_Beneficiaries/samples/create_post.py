from beem import Steem
steem = Steem(
    keys=["<priv_key>"],
)

beneficiaries = [
    {'account': 'crokkon', 'weight': 1000},
    {'account': 'holger80', 'weight': 1000},
]


steem.post(
    "Benef test with beem",
    "Benef test",
    author="beemtutorials",
    permlink="beemtutorials-test-post-benefs-2",
    tags="beem test test-post",
    beneficiaries=beneficiaries,
)

