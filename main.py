from functions import *
import time

print("Program Started! \n")


def execute():
    print("Its time, running program.")
    channel_id = "UCtHaxi4GTYDpJgMSGy7AeSw"
    channel_name = get_channel_name(channel_id=channel_id, youtube_api_key=YOUTUBE_API_KEY)
    videos = yt_retrive(channelId=channel_id, maxResults=2, API_KEY=YOUTUBE_API_KEY)
    days = days_ago(videos[0][1])
    print(f"Days ago: {days}")
    array = load_array("save.txt")

    if days == 0 and videos[0][0] != array[0]:
        print("New vid")
        create_tweet(f"{channel_name} just posted a new video! https://www.youtube.com/watch?v={videos[0][2]}")
    else:
        create_tweet(f"It has been {days} days since {channel_name} posted a video.")


while True:
    # get the current time
    current_time = time.localtime()
    print(current_time.tm_min)

    # check if it's time to run the program
    if current_time.tm_hour == 22 and current_time.tm_min == 0:
        execute()

    # sleep for two minute
    time.sleep(120)
