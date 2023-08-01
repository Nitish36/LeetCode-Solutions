import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    condition = tweets['content'].str.len()>15
    df = tweets.loc[condition,['tweet_id']]

    return df
