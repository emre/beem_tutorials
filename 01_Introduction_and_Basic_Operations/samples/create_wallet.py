from beem import Steem
steem = Steem()
steem.wallet.wipe(True)
steem.wallet.create("emre")
steem.wallet.unlock("emre")
steem.wallet.addPrivateKey("5HqmfJsgKhnsqu5aUV5Pp7wsuTbNGH791zUibBgSG7b2PzVcGnk")
