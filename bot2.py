from instapy import InstaPy
import requests

# Meaning Cloud
url = "https://api.meaningcloud.com/sentiment-2.1"

# Login and Quota Section
session = InstaPy(username="whomastank", password="10101TEST", headless_browser=True)
session.login()
session.set_quota_supervisor(enabled=True, peak_comments_daily=10, peak_comments_hourly=10, peak_follows_daily=20, peak_likes_daily=50, peak_likes_hourly=20)

# Like Section
session.like_by_tags([ "drawing", "doodle", "characterdesign", "illustrations", "lineart", "procreate"],
    amount=2)
session.set_dont_like([
    "nsfw", "naked", "porn", "ass", "assworship", "besties", "rightwinger",
    "asiangirl", "assday", "bikinibody", "beautylogger", "boho",
    "curvygirls", "date", "dm", "edm", "girlsonly", "gloves", "eggplant",
    "hustler", "kissing", "lulu", "milf", "models", "nudity", "nasty", "petite", "redhead",
    "prettygirl", "trump", "letsgobrandon", "bbl", "swole", "shower", "bodybuilder", "undies",
    "Youngmodel", "onlyfans", "america", "maga", "qanon", "q", "buildthewall", "rightwing", "kungflu",
    "progun", "alllivesmatter", "prolife", "liberalisamentaldisorder", "redwave", "conservatives", "trumptrain",
    "makeamericagreatagain", "politics"])
session.like_by_feed(amount=15, randomize=True, unfollow=True, interact=True)

# Follow Section
session.set_do_follow(True, percentage=50)
session.follow_by_tags(["drawing", "doodle", "characterdesign", "illustrations", "lineart", "procreate"],
                       amount=3)
session.follow_user_following(['illosketchbook', 'baileyillustration', 'penusbmic', 'faunwood', 'laurenmarxart'],
                              amount=3, randomize=True)

# Comment/Reply Section
session.set_use_meaningcloud(enabled=True, license_key='89f89a74a5603be4f79c20f06b2dee9c', polarity="P")
session.set_use_yandex(enabled=True, API_key='pdct.1.1.20211117T151613Z.48ea7bd44be43a7e.0b163e894468e7f2a44b81c742e4654ed53a967d',
                       match_language=True, language_code="en")
#session.set_do_comment(True, percentage=30)
session.set_do_reply_to_comments(enabled=True, percentage=14)
session.set_comment_replies(replies=[u"😁😁😁", u"😍😍😍😍", u"👏🏼😉"], media="Photo")

#session.set_user_interact(amount=2, percentage=70, randomize=False, media="Photo")
session.set_do_like(enabled=True, percentage=94)

#session.set_comments(["Nice!", "Sweet!", u"🧑‍🍳🤌", u"🙌🏻"])

session.end()