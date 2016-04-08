import sys
import twitter_data_types
import tweet_hasher
import csv

if len(sys.args) != 3 & len(sys.args) != 5:
    print("Error, needs 2 arguments (user_input,tweet_input) or 4 arguments (user_input,tweet_input,user_output,tweet_output)")
    quit()

user_in = sys.args[1]
tweet_in = sys.args[2]

user_out = user_in+".out"
tweet_out = tweet_in+".out"

if len(sys.args) == 5:
    user_out = sys.args[3]
    tweet_out = sys.args[4]

tweet_hasher = twitter_hasher.tweet_hasher()
user_hasher = twitter_hasher.user_hasher(tweet_hasher)

with open(tweet_in) as tweets:
    inFile = csv.reader(tweets)
    for row in inFile:
        tweet_hasher.train(twitter_data_types.tweet(row[0],row[1],row[2],row[3],row[4]))

with open(user_in) as users:
    inFile = csv.reader(users)
    for row in inFile:
        user_hasher.train(twitter_data_types.user(row[0],row[1],row[2],row[3],row[4]))
        
with open(tweet_in) as tweets:
    inFile = csv.reader(tweets)
    for row in inFile:
        newtweet = tweet_hasher.convert(twitter_data_types.tweet(row[0],row[1],row[2],row[3],row[4])) 
        print(newtweet.text+"\t"+newtweet.poster_id+"\t"+newtweet.date+"\t"+newtweet.tweet_id+"\t"+newtweet.retweets)   
