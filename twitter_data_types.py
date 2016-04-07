class user(object):
    def __init__(self, screen_name = "USER_NAME",followers = -1, friends = -1, tweets = -1, user_id = -1):
        self.screen_name = screen_name
        self.followers = followers
        self.friends = friends
        self.tweets = tweets
        self.user_id = user_id
    def to_json(self):
        return {"screen_name":self.screen_name,"followers":self.followers,"friends":self.friends,"tweets":self.tweets,"user_id":self.user_id}

class tweet(object):
    def __init__(self, text = "THIS IS A TWEET", poster_id = -1, date = None, tweet_id = -1, retweets = -1):
        self.text = text
        self.poster_id = poster_id
        self.date = date
        self.tweet_id = tweet_id
        self.retweets = retweets
    def to_json(self):
        return {"text":self.text, "poster_id":self.poster_id, "date":self.date, "tweet_id":self.tweet_id, "retweets":self.retweets}