import twitter_data_types
import tweet_hasher

t = tweet_hasher.tweet_hasher(forceWordSize = True, matchCases = True)

t.train(12,"this is a test!",0)
t.train(12,"also a #test",12)
t.train(23,"Something else? ;)",23)    

print(t.convert(12,"this is a test!",0))
print(t.convert(12,"also a #test",12))
print(t.convert(23,"Something else? ;)",23))


u = twitter_data_types.user("bob",25,32,0,12)
uh = tweet_hasher.user_hasher(t)

print(u.to_json())
print(uh.convert(u).to_json())
