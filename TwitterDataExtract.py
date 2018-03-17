
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "795235645048246273-CnpWvTLYOLgwrPcJK28OvXxMcL2EJSg"
access_token_secret = "q3itIa19sNZWXwqF4st5YKL87JnFYIgWy0HuvO0qg7LND"
consumer_key = "KlHPE7a0xMZVPRo5Yu8SwhPUT"
consumer_secret = "CeqbdVewkFdzdI0OcGZSwp06PSa9fn7atpddcCupJNu0Pt1CoG"



class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

   
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

   
    stream.filter(track=['#sarcasm', '#sarcastic'])
