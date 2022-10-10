import random
from time import sleep
from instagrapi import Client
from cred import *

client = Client()

class StartupRoutine:
    def __init__(self, welcome, insta_username, insta_password, tfa, hashtag, caption, pause):
        self.welcome = welcome
        self.insta_username = insta_username
        self.insta_password = insta_password
        self.tfa = tfa
        self.hashtag = hashtag
        self.caption = caption
        self.pause = pause

startUp = StartupRoutine(print("Instagrapi Bot v.0.0.1 by deusopus@gmail.com"), insta_username, insta_password, input("Enter your 2FA code: "), random.choice(hashtags), random.choice(captions), random.randrange(2400, 4800))

startUp.welcome
startUp.tfa

client.login(startUp.insta_username, startUp.insta_password, verification_code=startUp.tfa)

posts = client.hashtag_medias_recent(startUp.hashtag)

for i, media in enumerate(posts):
        
        client.media_like(media.id)
        print(f"Liked post {i+1} with #{startUp.hashtag} by @{media.user.username}")
        wait = startUp.pause
        print(f"Sleeping for {wait} seconds")
        sleep(wait)
        
        if i % 5 == 0 and i % 3 == 0:
            
            client.user_follow(media.user.pk)
            print(f"Followed @{media.user.username}")
            wait = startUp.pause
            print(f"Sleeping for {wait} seconds")
            sleep(wait)

            caption = startUp.caption
            client.media_comment(media.id,caption)
            print(f"Commented with: {caption} on post {i+1}")
            wait = startUp.pause
            print(f"Sleeping for {wait} seconds")
            sleep(wait)
