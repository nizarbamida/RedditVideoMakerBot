import requests
from utils.console import print_step


def post_tiktok(video_path):
    """
    Post a video to TikTok.
    """

    payload = {
    "post": "#reddit #redditstories #askreddit #funnyreddit #bestofreddit #redditcringe #reddittopposts #reddittop #redditcompilation #redditdumb ##reddit",
    "platforms": ["tiktok"],
    "mediaUrls": [video_path]
    }

    # Live API Key
    headers = {'Content-Type': 'application/json', 
            'Authorization': 'Bearer 3AW4FRF-0AJ43GY-NE6SW9X-0E3EQB7'}

    r = requests.post('https://app.ayrshare.com/api/post', 
        json=payload, 
        headers=headers)

    if r.status_code == 200:
        print_step("Successfully posted to TikTok!")
        print_step(r.json())

    else:
        print_step("Failed to post to TikTok.")
        print_step(r.text)