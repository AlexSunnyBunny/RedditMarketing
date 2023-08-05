import time
from random import randint
import praw
from requests import Session

USERNAME = "HERE"
PASSWORD = "HERE"
CLIENT_ID = "HERE"
CLIENT_SECRET = "HERE"

class Reddit:
    def __init__(self, config):

        self.reddit = praw.Reddit(
            client_id=config["CLIENT_ID"],
            client_secret=config["CLIENT_SECRET"],
            username=config["USERNAME"],
            password=config["PASSWORD"],
            user_agent="pass",
        )
        self.reddit.validate_on_submit = True

    def post(self, subreddit, title, url):
        if url:
            submission = self.reddit.subreddit(subreddit).submit(title=title, url=url, nsfw=True)
        #   else:
        #       submission = self.reddit.subreddit(subreddit).submit(
        #           title=title, selftext=text
        #       )
        return submission


def main():

    config = {
        "CLIENT_ID": CLIENT_ID,
        "CLIENT_SECRET": CLIENT_SECRET,
        "USERNAME": USERNAME,
        "PASSWORD": PASSWORD,
    }

    reddit = Reddit(config)

    data = {'subs': [], 'titles': [], 'links': []}

    for k, v in data.items():
        with open(f"{k}.txt") as fp:
            data.update({k: fp.read().splitlines()})

    post_list = list(zip(data['subs'], data['titles'], data['links']))

    for post in post_list:
        print(f"Posting to {post[0]}:\n{post[1]}\n{post[2]}\n\n")
        sub = reddit.post(post[0], title=post[1], url=post[2])
        print('posted.. sleeping now')
        time.sleep(randint(230, 380))

if __name__ == "__main__":
    main()
