from beem import Steem
steem = Steem(
    keys=["<private_posting_wif>"]
)
steem.post(
    "My title for the post",
    "Beem is awesome! (post body)",
    author="beemtutorials",
    permlink="beemtutorials-test-post",
    app="myapp/0.0.1",
    tags="beem test test-post"
)