from typing import Any, Dict, List
import tweepy
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from src.constants import BRAZIL_WOE_ID
from src.connection import trends_collection

def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    

    trends = api.trends_place(woe_id)

    return trends[0]['trends']

def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})

    return trends

def save_trends() -> None:

    auth = tweepy.OAuthHandler(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET)
    auth.seth_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)