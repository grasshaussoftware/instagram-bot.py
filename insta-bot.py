import random
from time import sleep
from instagrapi import *
from credentials import *

client = Client()

tfa = input('Enter 2FA code: ')
client.login(insta_username, insta_password, verification_code=tfa)

while True:
    hashtag = random.choice(hashtags)
    caption = random.choice(captions)
    wait = random.randrange(600,1200)

    target_post = client.hashtag_medias_recent(hashtag)
    for i, media in enumerate(target_post):
        client.media_like(media.id)
        print(f"Liked post {i+1} with #{hashtag} by @{media.user.username}")
        print(f"Sleeping for {wait} seconds")
        sleep(wait)
        if i % 5 == 0 and i % 3 == 0:
            client.user_follow(media.user.pk)
            print(f"Followed @{media.user.username}")
            print(f"Sleeping for {wait} seconds")
            sleep(wait)
            
            client.media_comment(media.id,caption)
            print(f"Commented with: {caption} on post {i+1}")
            print(f"Sleeping for {wait} seconds")
            sleep(wait)
