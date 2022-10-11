import random
from time import sleep
from instagrapi import *
from cred002 import *

client = Client()

class Engine:
    def __init__(self, welcome, insta_username, insta_password, tfa, pub_pk, pub_id, pub_user, hashtag, caption, timer):
        self.welcome = welcome
        self.insta_username = insta_username
        self.insta_password = insta_password
        self.tfa = tfa
        self.pub_pk = pub_pk
        self.pub_id = pub_id
        self.pub_user = pub_user
        self.hashtag = hashtag
        self.caption = caption
        self.timer = timer

startUp = Engine(print("Instagrapi Bot v.0.0.1 by deusopus@gmail.com"), insta_username, insta_password, input("Enter your 2FA code: "), client.media.user.pk, client.media.id, client.media.user.username, random.choice(hashtags), random.choice(captions), random.randrange(2400, 4800))

startUp.welcome()
startUp.tfa()

client.login(startUp.insta_username, startUp.insta_password, verification_code=startUp.tfa)

class Core:
    def __init__(self, pubs, like, comment, follow):
        self.pubs = pubs
        self.like = like
        self.comment = comment 
        self.follow = follow   

instagram = Core(client.hashtag_medias_recent(startUp.hashtag)), client.media_like(startUp.pub_id), client.media_comment(startUp.pub_id,startUp.caption), client.user_follow(startUp.pub_pk)

for i, items in enumerate(instagram.pubs):

    instagram.like()
         
    print(f"Liked post {i+1} with #{startUp.hashtag} by @{startUp.pub_user}")
    
    print, sleep(f"Pausing for {startUp.timer} seconds")
        
    if i % 5 == 0 and i % 3 == 0:

        instagram.follow()
    
        print(f"Followed @{startUp.pub_user}")

        print, sleep(f"Sleeping for {startUp.timer} seconds")

        caption = startUp.caption

        instagram.comment()

        print(f"Commented with: {startUp.caption} on post {i+1}")

        print, sleep(f"Sleeping for {startUp.timer} seconds")
