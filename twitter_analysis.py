import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2019-08-01") \
        .setUntil("2020-02-28") \
        .setMaxTweets(10)

    #List of object gets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    #Iterating through tweets list. Storing them temp in tweet variable
    #Get text and store it as list inside text_tweets
    text_tweets = [[tweets.text] for tweet in tweets]
    print(text_tweets)

get_tweets()