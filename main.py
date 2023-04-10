import asyncio
import asyncpraw
from telegram import Bot
import yaml
import os
import logging

REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

with open('search-config.yml') as f:
    search_config = yaml.safe_load(f)

bot = Bot(TELEGRAM_API_TOKEN)

async def check_submissions():
    try:
        for sub in search_config['subreddits']:
            async with asyncpraw.Reddit(
                client_id=REDDIT_CLIENT_ID,
                client_secret=REDDIT_CLIENT_SECRET,
                user_agent='telegram-bot/0.0.1'
            ) as reddit:
                subreddit = await reddit.subreddit(sub['name'])
                async for submission in subreddit.stream.submissions(skip_existing=True):
                    if any(x in submission.title.lower() for x in sub['keywords']) and submission.link_flair_text in sub['flairs']:
                        logging.info(f'Found new submission in r/{sub["name"]} subreddit: {submission.title}')
                        message = f'New submission in r/{sub["name"]} subreddit:\n{submission.title}\n{submission.url}'
                        await bot.send_message(TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        error_message = f'Error: {e}'
        await bot.send_message(TELEGRAM_CHAT_ID, error_message)
        logging.error(error_message)
    logging.info('Sleeping for 10 seconds')
    await asyncio.sleep(60)

async def main():
    while True:
        await check_submissions()

if __name__ == '__main__':
    logging.info('Starting bot')
    asyncio.run(main())
