import os

from beem import Steem
s = Steem(
    ["https://api.steemit.com",],
    keys=[os.getenv("POSTING_KEY"), ]
)

