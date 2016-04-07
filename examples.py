import twitter_data_types
import tweet_hasher

t = tweet_hasher.tweet_hasher(forceWordSize = True, matchCases = True)

t1 = twitter_data_types.tweet("this is a test!",12,0,123,5)
t2 = twitter_data_types.tweet("also a #test",12,0,124,100)
t3 = twitter_data_types.tweet("Something else? ;)",23,0,125,0)

tweets = [t1,t2,t3]

for tweet in tweets:
	t.train(tweet)

for tweet in tweets:
	print(tweet.to_json())
	print(t.convert(tweet).to_json())


u = twitter_data_types.user("bob",25,32,0,12)
uh = tweet_hasher.user_hasher(t)

print(u.to_json())
print(uh.convert(u).to_json())
