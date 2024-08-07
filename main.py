import requests
import time

# Twitter API credentials
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAABvMtQEAAAAAK2PmkGSdWfMKpRwmZccSu0lh3Yo%3D0Ok48ZDAUeXJsvJPHKe04pjfXVj0LrxOulzjpJFz9xfdSCsJfK'  # Use your Bearer Token from Twitter API v2

# Twitch API credentials
TWITCH_CLIENT_ID = 't9zsu3uuytsuvhi0yy8n3eodnmfd3j'
TWITCH_ACCESS_TOKEN = '4fz0720zdar2d9fxi3qrz4uyhhjuev'
TWITCH_USER_LOGIN = 'MohaXGaming_'

# Function to check Twitch stream status
def check_twitch_stream():
    url = f'https://api.twitch.tv/helix/streams?user_login={TWITCH_USER_LOGIN}'
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {TWITCH_ACCESS_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get('data'):
        return True, data['data'][0]['title']
    else:
        return False, None

# Function to post tweet using Twitter API v2
def post_tweet(message):
    url = 'https://api.twitter.com/2/tweets'
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    json_data = {
        'text': message
    }
    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Tweet posted successfully")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main function to check stream status and tweet
def main():
    is_live, stream_title = check_twitch_stream()
    if is_live:
        tweet_message = f"I'm live on Twitch! 🎮\n{stream_title}\nWatch here: https://www.twitch.tv/{TWITCH_USER_LOGIN}"
        post_tweet(tweet_message)
    else:
        print("Stream is not live")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)
