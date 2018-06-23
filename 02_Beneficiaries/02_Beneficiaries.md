<img src="https://steemitimages.com/0x0/https://cdn.utopian.io/posts/d563a408c062506aed88befbe7781399184fbeem-logo.png">

#### Repository of Beem
[https://github.com/holgern/beem](https://github.com/holgern/beem)    

#### Tutorial Content

- You will learn about the beneficiaries and how to set it via Beem on post creation.

#### Requirements

- Python 2.7.x or 3.4+
- Basic Python knowledge

***

In the first part of [this series](/@emrebeyler/beem-tutorials-1-introduction-to-beem-and-creating-a-post-with-it), we had a sweet introduction to the library and created a post. One of the options of post() function of Beem is the **beneficiaries**.

#### Beneficiaries

With the recent popularity of dapps on top of STEEM, [beneficiary option](https://github.com/steemit/steem/issues/773) has been known widely. It's basically an option where you can share your author rewards with other accounts on your posts. Currently, all beneficiary rewards are paid on STEEM Power form regardless the post has %50 SBD/%50 SP option enabled or not.

#### Setting Beneficiaries on Beem

```python
from beem import Steem
steem = Steem(
    keys=["<private_wif>"],
)

beneficiaries = [
    {'account': 'crokkon', 'weight': 1000},
    {'account': 'holger80', 'weight': 1000},
]


resp = steem.post(
    "Benef test with beem",
    "Benef test",
    author="beemtutorials",
    permlink="beemtutorials-test-post-benefs",
    tags="beem test test-post",
    beneficiaries=beneficiaries,
)

print(resp)
```

This is the same example on the first tutorial except on extra ```beneficiaries```. It's a list of python dicts where you store account names and their reward weights. (sharing percentages.)

This code will give an output like that:

```
{
    'expiration': '2018-06-23T16:41:40',
    'ref_block_num': 51293,
    'ref_block_prefix': 1003704839,
    'operations': [
        ['comment', {
            'parent_author': '',
            'parent_permlink': 'post',
            'author': 'beemtutorials',
            'permlink': 'beemtutorials-test-post-benefs',
            'title': 'Benef test with beem',
            'body': 'Benef test',
            'json_metadata': '{"app": "myapp/0.0.1", "tags": ["post", "beem", "test"]}'
        }],
        ['comment_options', {
            'author': 'beemtutorials',
            'permlink': 'beemtutorials-test-post-benefs',
            'max_accepted_payout': '1000000.000 SBD',
            'percent_steem_dollars': 10000,
            'allow_votes': True,
            'allow_curation_rewards': True,
            'extensions': [
                [0, {
                    'beneficiaries': [{
                        'account': 'crokkon',
                        'weight': 1000
                    }, {
                        'account': 'holger80',
                        'weight': 1000
                    }]
                }]
            ]
        }]
    ],
    'extensions': [],
    'signatures': ['1f689b34de1afedb55556dba10fe7f8841396513ea1961da797e3babb732b5e3a22465a23ff3d77d231a563cc7731d224480b67e1d4d0036b4d94214f7ef701683']
}
```

As you can see from the output, beneficiaries are actually set in the ```CommentOption``` operation. We basically push two operations (```Comment``` and ```CommentOption``` in one transaction to set beneficiaries. 

**Note:** ```'weight': 1000``` means that %10 of the author rewards. Steem blockchain uses same weight convention on blockchain code. Just divide by 100 and get the value in percent when you see weight in any operation.

<center><img src="https://cdn.steemitimages.com/DQmTJhACJszmSbb15VaaU2rExopefKAhoiFJswvj6pFUND3/Screen%20Shot%202018-06-23%20at%207.56.57%20PM.png"></center>

<center><sup>steemd representation of the post</sup></center>


#### Limitations

- You cannot specify more than 8 beneficiaries.
- Total weight cannot be greater than 10000 (Obviously).
- Account names must be specified in sorted order.
- While it's possible to set beneficiaries after the post creation, it's not possible if the post got a vote or a comment. It's highly suggested to bundle the operations. (Beem already does that.)
- Once beneficiaries set, there is no way to remove or update them for a particular post.


#### Curriculum

- [Introduction to Beem and creating a post with it](/@emrebeyler/beem-tutorials-1-introduction-to-beem-and-creating-a-post-with-it)
- [Setting beneficiaries with Beem](/@emrebeyler-beem-tutorials-2-setting-beneficiaries=with-beem)

#### Sample Codes

[Samples](https://github.com/emre/beem_tutorials/tree/master/02_Beneficiaries/samples)




