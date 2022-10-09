import re
import random
from time import sleep
from instagrapi import Client
from credentials import *

def login(client):
    client = Client()
    tfa = input('Enter 2FA code: ')
    if not re.match("^\\d+$", tfa):
        print ("Error! Only letters a-zA-Z_0-9 allowed!")
        sys.exit()
    client.login(insta_username, insta_password, verification_code=tfa)
    return(client)

def main(client, hashtag, x, y, z):
    target_post = client.hashtag_medias_recent(hashtag)
    for i, media in enumerate(target_post):
        client.media_like(media.id)
        print(f"Liked post {i+1} with #{hashtag} by @{media.user.username}")
        print(f"Sleeping for {x} seconds")
        sleep(x)
        if i % 5 == 0 and i % 3 == 0:
            client.user_follow(media.user.pk)
            print(f"Followed @{media.user.username}")
            print(f"Sleeping for {y} seconds")
            sleep(y)
            caption = random.choice(captions)
            client.media_comment(media.id,caption)
            print(f"Commented with: {caption} on post {i+1}")
            print(f"Sleeping for {z} seconds")
            sleep(z)
    return(client, hashtag, x, y, z)

while True:
    main(client = login(0), hashtag = random.choice(hashtags), x = random.randrange(350,700), y = random.randrange(350,700), z = random.randrange(350,700))