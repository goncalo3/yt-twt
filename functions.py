from googleapiclient.discovery import build
from datetime import datetime
import tweepy
import pickle
from keys import *


def days_ago(date):
    # Convert the date to a datetime object
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')

    # Calculate the difference between the given date and the current date
    diff = datetime.now() - date

    # Return the number of days in the difference
    return diff.days


def save_array(array, filename):
    # Open the file in binary write mode
    with open(filename, 'wb') as file:
        # Use the pickle.dump() function to serialize the array and write it to the file
        pickle.dump(array, file)

    print('Array saved to file successfully!')


def load_array(filename):
    # Open the file in binary read mode
    with open(filename, 'rb') as file:
        # Use the pickle.load() function to deserialize the array from the file
        array = pickle.load(file)

    return array


def yt_retrive(channelId, maxResults, API_KEY):
    # Use the YouTube API's search.list method to retrieve the latest videos from the specified channel
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        part='id,snippet',
        type='video',
        order='date',
        maxResults=maxResults,
        channelId=channelId
    )
    response = request.execute()

    # Extract the video title, publishing date, and video ID from the API response
    videos = []
    for item in response['items']:
        video_title = item['snippet']['title']
        publishing_date = item['snippet']['publishedAt']
        video_id = item['id']['videoId']
        videos.append([video_title, publishing_date, video_id])
    return videos


def create_tweet(text):
    client = tweepy.Client(
        consumer_key=TWT_CONSUMER_KEY,
        consumer_secret=TWT_CONSUMER_SECRET,
        access_token=TWT_ACCESS_TOKEN,
        access_token_secret=TWT_ACCESS_TOKEN_SECRET
    )
    client.create_tweet(text=text)
    print(f"Tweeted: \"{text}\"")
