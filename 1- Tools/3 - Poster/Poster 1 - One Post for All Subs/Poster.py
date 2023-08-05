from time import sleep
from random import randint
import praw
from requests import Session


class Poster:
    def __init__(self):
        self.session = Session()
        self.list_of_links = list()
        self.list_of_titles = list()
        self.list_of_subs = list()

        # Put your proxy here
        self.proxy = "evtutnew-rotate:lw069c4zx5r1@45.9.123.6:80"

        # Loading data files
        self.file_of_titles = 'titles.txt'
        self.file_of_links = 'links.txt'
        self.file_of_subs = 'subs.txt'

        # Reddit API Credentials
        self.id = ""
        self.secret = ""
        self.username = ""
        self.password = ""

        # Praw credentials
        self.reddit = praw.Reddit(user_agent='pass',
                                  client_id=self.id,
                                  client_secret=self.secret,
                                  username=self.username,
                                  requestor_kwargs={'session': self.session},
                                  password=self.password)
        self.reddit.validate_on_submit = True

        # Main
        try:
            self.initialize()
            self.run()
        except KeyboardInterrupt:
            print('\n\n\nThis program has fucked up.')


    def initialize(self):
        with open(self.file_of_subs, 'r', encoding='utf-8') as reader:
            self.list_of_subs = reader.read().strip().split('\n')
        with open(self.file_of_titles, 'r', encoding='utf-8') as reader:
            self.list_of_titles = reader.read().strip().split('\n')
        with open(self.file_of_links, 'r', encoding='utf-8') as reader:
            self.list_of_links = reader.read().strip().split('\n')

    def run(self):
        for sub in self.list_of_subs:
            for link, title in zip(self.list_of_links, self.list_of_titles):
                try:
                    self.session.proxies = {'http': 'http://' + self.proxy, 'https': 'https://' + self.proxy}
                    # ext_ip = self.session.get('http://checkip.dyndns.org')
                    # print(ext_ip.text)
                    print(f"Posting to {sub}:\n{title}\n{link}\n\n")
                    self.reddit.subreddit(sub).submit(title=title, url=link, nsfw=False)
                    print('Posted.. sleeping now..')
                    self.session.close()
                    sleep(randint(3600, 4000))
                except:
                    print(f"Skipping this  {sub}:\n{title}\n{link}\n\n")
                    pass

if __name__ == "__main__":
    Poster()
