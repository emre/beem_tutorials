from beem import Steem
s = Steem(
    ["https://api.steemit.com",]
)

print(s.get_blockchain_version())