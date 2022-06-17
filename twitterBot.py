from datetime import date

import config
import tweepy

auth = tweepy.OAuthHandler(config.consumerKey, config.consumerKeySecret)
auth.set_access_token(config.accessToken, config.accessTokenSecret)

api = tweepy.API(auth)

number = 0

today = date.today()
textToday = today.strftime("%B %d, %Y")
api.update_status(f"Today is {textToday} and it is 4:30 EST. Wake up NOW and lift weights.")