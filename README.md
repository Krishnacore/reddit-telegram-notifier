# Telegram Reddit bot

This is a Python script that uses the Telegram API and the Reddit API to send a message to a Telegram chat whenever a new submission is made to a subreddit that matches certain keywords.

## Installation

Install the required Python packages by running `pip install -r requirements.txt` in your terminal.

## Usage

1. Create a search-config.yml file in the root directory of the repository with the following structure:

```yaml
subreddits:
  - name: example_subreddit
    keywords:
      - keyword1
      - keyword2
    flairs: []
  - name: another_subreddit
    keywords:
      - keyword3
    flairs: []
```

Replace `example_subreddit`, `another_subreddit`, `keyword1`, `keyword2`, and `keyword3` with the names of the subreddits and keywords you want to search for.

2. Set the following environment variables:

REDDIT_CLIENT_ID: Your Reddit client ID.
REDDIT_CLIENT_SECRET: Your Reddit client secret.
TELEGRAM_API_TOKEN: Your Telegram API token.
TELEGRAM_CHAT_ID: The chat ID of the Telegram chat you want to send messages to.

3. Run the script by running python app/main.py in your terminal. The script will run continuously and send messages to the Telegram chat whenever a new submission is made to a subreddit that matches the keywords specified in `search-config.yml`.
