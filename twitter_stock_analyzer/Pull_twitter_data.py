import pandas as pd
import snscrape.modules.twitter as sntwitter




def scrape_tweets(name, amount):
    scraper = sntwitter.TwitterSearchScraper(name)
    tweets = []
    for i, tweet in enumerate(scraper.get_items()):
        if i == amount:
            break
        data = [tweet.date,
                tweet.id,
                tweet.content,
                tweet.user.username,
                tweet.likeCount,
                tweet.retweetCount,
                ]
        tweets.append(data)
        if i> amount:
            break
    tweet_df = pd.DataFrame(tweets, columns = ["date", "id", "content", "username", "like_count", "retweet_count"])
    return tweet_df