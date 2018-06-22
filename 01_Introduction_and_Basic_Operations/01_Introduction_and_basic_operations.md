<img src="https://steemitimages.com/0x0/https://cdn.utopian.io/posts/d563a408c062506aed88befbe7781399184fbeem-logo.png">

#### Tutorial Content

- You will learn how to get started with Beem.
- You will learn how to create a post via Beem.

#### Requirements

- Python 2.7.x or 3.4+
- Basic Python knowledge


#### Introduction

[Beem](http://beem.readthedocs.io/en/latest/) is an alternative python library by @holger80 to interact with the STEEM blockchain. 

After seeing it's constant development and getting very good feedbacks about the library, I have decided to switch to beem for my bots and scripts.

I will learning Beem in the next couple of weeks and will write my experience on it as a tutorial series. Welcome to the first part of it. 

#### Installation

Installing the library is already covered well in the official [documentation](http://beem.readthedocs.io/en/latest/installation.html). It supports both Python2.7+ and Python 3.4+ versions.

For the Osx, I have followed these steps to install:
```
$ mkvirtualenv -p python3.6 beemtutorials
$ pip install beem
```

Note: First line creates a virtual environment. It's the industry standard on python development at the moment. I highly suggest working
with virtual environments if you don't practise that way already.

#### Setting up the Steem instance

```python
from beem import Steem
s = Steem()

print(s.get_blockchain_version())
```

You will see an output as ```0.19.2```.

This is the main class we use to interact with the blockchain. You can see the parameters
and their definitions at [source code/steem.py](https://github.com/holgern/beem/blob/77f41933b7e2f37638dc1df900efcf9ea2a7d7e6/beem/steem.py#L37). However, you don't really need all of them.
I will cover the important ones.

##### Setting a node

The first parameter is a list of nodes you want to connect. Let's run the same example with a different node:

```python
from beem import Steem
s = Steem(
    ["https://api.steemit.com",]
)

print(s.get_blockchain_version())
```

You will see the output has changed as ```0.19.4``` since api.steemit.com runs a newer version of steemd.

##### Setting keys

```python
from beem import Steem
s = Steem(
    ["https://api.steemit.com",],
    keys=["<private_key_1>", "<private_key_2>"]
)
```

Keys are private keys you have on steem accounts. If you want to 
create a post, you need *posting private key* entered here. However, storing
keys raw in source codes may not be the best solution since you may push your
private keys to the repositories.

There are a couple of options to solve that issue:

- Using environment variables

```python
import os

from beem import Steem
s = Steem(
    ["https://api.steemit.com",],
    keys=[os.getenv("POSTING_KEY"), ]
)
```

This example gets the posting key from environment variables. You need to set
that ```POSTING_KEY``` variable before executing the code.

```
POSTING_KEY=<posting_key_of_account> python script.py
```

- Using Beem's wallet 

Beem has a wallet implementation to make account/wallet related options more practical.
The following code creates a wallet with ```unique-pass``` passphrase and adds a private key
into the wallet.

```python
from beem import Steem
steem = Steem()
steem.wallet.create("unique-pass")
steem.wallet.unlock("unique-pass")
steem.wallet.addPrivateKey("<posting_wif>")
```

After doing that, whenever you need to broadcast something you can unlock the wallet by
setting ```UNLOCK``` environment variable.

Note: If you already created a wallet and don't remember the password, you can wipe the old
wallet by

```python
steem.wallet.wipe(True)
```

before creating a new wallet. Otherwise you will get an error that there is already a wallet
exists.

You can also use the command line tool (```$beempy```) ships with the package to perform 
wallet related issues.


To create wallet:

```
$ beempy createwallet
```

To add private keys to the wallet:

```
$ beempy addkey <your_private_key>
```

**Note:** Beem stores wallet information on a SQLITE database. It's stored at
 ```~/Library/Application\ Support/beem/beem.sqlite``` for my OSX setup. You can
 see where it's located from the steem.config object:
 
 ```python
from beem import Steem
steem = Steem()
print(steem.config.data_dir)
```

**Note:** If you use Beem's wallet, you don't need to use the ```keys``` parameter
of Steem() since Beem will get keys from the unlocked wallet.

#### Creating a Post

You don't need any interface (Steemit, Busy, etc.) to create posts. Let's do it with Beem.

**Note:** Posts are actually are *Comment* objects in the steem blockchain. If a comment doesn't have any parent, that means it's a post.

I will explicitly set private posting key to keep things simple.

```python
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
```

You can see the created post [here](https://steemit.com/test/@beemtutorials/beemtutorials-test-post). Let's see the possible parameters for the post:

The first two parameter are obviously *post title* and *post body*. However, post() functions can get lots of keyword arguments.

| Parameter        | Value                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| author           | Author of the post. Not needed if you set a default account via beempy.                                                      |
| permlink         | Permlink of the post. Should be unique together with author and permlink. If not set, beem will auto-generate it from title. |
| reply_identifier | Identifier (Ex: @author/permlink) for the parent post. Not needed if you create a new post. Required for comments.           |
| json_metadata    | Custom json metadata of the post. If you develop an app and need customized info, you can put it here.                       |
| comment_options  | Some options for the post. You can specify: max_accepted_payout, percent_steem_dollars, allow_curation_rewards etc.          |
| community        | The community we're posting into. Example: Utopian was using "utopian" here. Overrides json_metadata.community.               |
| app              | The app used for creating the post. Busy, Steemit and other dapps puts their information here like "Busy/2.4.0"              |
| tags             | A list of tags for the post. Example: "steem steemit utopian beem"                                                           |
| beneficiaries    | A list of beneficiaries for reward sharing.                                                                                  |
| self_vote        | If you set this as True, author will upvote the created post right after the creation.                                       |

Beneficiaries is an interesting option here, we will discuss it in the upcoming tutorials in this series.

#### Curriculum

- [Introduction to Beem and creating a post with it](@emrebeyler/introduction-to-beem-and-creating-a-post-with-it)


#### Repository of Beem
[https://github.com/holgern/beem](https://github.com/holgern/beem)    

#### Sample Codes:
[https://github.com/emre/beem_tutorials/tree/master/01_Introduction_and_Basic_Operations/samples](https://github.com/emre/beem_tutorials/tree/master/01_Introduction_and_Basic_Operations/samples)



 

