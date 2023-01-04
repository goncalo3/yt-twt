# Youtube to Twitter Bot

Bot to tweet how long has been since a youtuber published a video.

Gets the video data from the youtube api
Saves it locally because double check if new vid (yes its redundant and completly useless but i felt like doing it).

If new video tweets the link to the new video;
Else tweets number of days since latestr video.

Still trying to figure out how to get it working on a docker container.

To use create a keys.py file containing:

TWT_CONSUMER_KEY,
TWT_CONSUMER_SECRET,
TWT_ACCESS_TOKEN,
TWT_ACCESS_TOKEN_SECRET,
YOUTUBE_API_KEY
    
