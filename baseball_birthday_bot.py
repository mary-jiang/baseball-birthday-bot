import tweepy
import logging
import os
import birthday_scraper

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

def main():
    api = create_api()

    birthday_boy_stats = birthday_scraper.birthday_boy_stats()
    status = "Happy birthday to " + birthday_boy_stats["name"] + "!"

    api.update_status(status=status)

if __name__ == "__main__":
    main()