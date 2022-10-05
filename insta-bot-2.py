import time
import random
from time import sleep
from instagrapi import Client
from credentials import *

client = Client()
tfa = input('Enter 2FA code: ')

client.login(insta_username, insta_password, verification_code=tfa)

hashtag = "cannabisculture"
captions = ["got pot?", "Check out our Linktr.ee/cannacoin", "www.cannacoin.org"] 
mediums = client.hashtag_medias_recent(hashtag)

caption = random.choice(captions)

def follow_follow():
    for i, media in enumerate(mediums):
        client.media_like(media.id) #like post with hashtag
        print(f"Liked number {i+1} of {media.user.username}")
        sleep(60)
        client.media_comment(media.id, caption) #make a comment from the list at random
        print(f"Commented {caption} under post number {i+1}")
        sleep(5)
        client.user_follow(media.user.pk) #follow on deck user
        print(f"Followed user {media.user.username}")
        sleep(217)
        #find their first "friend". a follower that they follow back.

while True:
    follow_follow()