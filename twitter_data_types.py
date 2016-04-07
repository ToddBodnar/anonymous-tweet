class user(object):
    def __init__(self, screen_name = "USER_NAME",followers = -1, friends = -1, tweets = -1, user_id = -1):
        self.screen_name = screen_name
        self.followers = followers
        self.friends = friends
        self.tweets = tweets
        self.user_id = user_id
    def to_json(self):
        return {"screen_name":self.screen_name,"followers":self.followers,"friends":self.friends,"tweets":self.tweets,"user_id":self.user_id}
