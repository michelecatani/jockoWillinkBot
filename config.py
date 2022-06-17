from dotenv import load_dotenv
load_dotenv()

import os

consumerKey = os.getenv('APIKey')
consumerKeySecret = os.getenv('APIKeySecret')
BearerToken = os.getenv('BearerToken')
clientID = os.getenv('clientID')
clientSecret=os.getenv('clientSecret')
accessToken=os.getenv('accessToken')
accessTokenSecret=os.getenv('accessTokenSecret')