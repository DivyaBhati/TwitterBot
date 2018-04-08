import csv
import tweepy

def stream_saver(search_terms):

    #These 4 are empty because you have to input your own keys and tokens on the
    #twitter developer website
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)

    class CustomStreamListener(tweepy.StreamListener):

        def on_status(self, status):
            print (status.author.screen_name, status.created_at, status.text)
            stattext = "@" + status.author.screen_name + " " + "Jason is soft!"
            api.update_status(stattext, status.id)
            # Writing status data

        def on_error(self, status_code):
            print >> sys.stderr, 'Encountered error with status code:', status_code
            return True

        def on_timeout(self):
            print >> sys.stderr, 'Timeout...'
            return True


    streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
    streamingAPI.filter(track=[search_terms])

    
#You have to put your twitter handle in here like '@realDonaldTrump'
twitterHandle = '@'

stream_saver(twitterHandle)