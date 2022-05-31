from random import randrange
from pytube import YouTube
from pathlib import Path
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from utils.console import print_step, print_substep
import random


def get_start_and_end_times(video_length, length_of_clip):

    random_time = randrange(180, int(length_of_clip) - int(video_length))
    return random_time, random_time + video_length


def download_background():
    """Downloads the background video from youtube.

    Shoutout to: bbswitzer (https://www.youtube.com/watch?v=n_Dv4JMiwK8)
    """
    videos = [["https://www.youtube.com/watch?v=-NzSWkfZ3-4", "assets/mp4/background1.mp4"],
    ["https://www.youtube.com/watch?v=H_7XOMO7nJE", "assets/mp4/background2.mp4"],
    ["https://www.youtube.com/watch?v=n_Dv4JMiwK8", "assets/mp4/background.mp4"] ]

    video_s = random.choice(videos)

    if not Path(video_s[1]).is_file():
        print_step(
            "We need to download the Minecraft background video. This is fairly large but it's only done once. 😎"
        )
        print_substep("Downloading the background video... please be patient 🙏")
        YouTube(video_s[0]).streams.filter(
            res="720p"
        ).first().download(
            "assets/mp4",
            filename= video_s[1].rsplit("/")[2]
        )
        print_substep("Background video downloaded successfully! 🎉", style="bold green")


def chop_background_video(video_length):
    videos = [["https://www.youtube.com/watch?v=-NzSWkfZ3-4", "assets/mp4/background1.mp4"],
    ["https://www.youtube.com/watch?v=H_7XOMO7nJE", "assets/mp4/background2.mp4"],
    ["https://www.youtube.com/watch?v=n_Dv4JMiwK8", "assets/mp4/background.mp4"] ]

    print_step("Finding a spot in the background video to chop...✂️")
    video_s = random.choice(videos)
    background = VideoFileClip(video_s[1])

    start_time, end_time = get_start_and_end_times(video_length, background.duration)
    ffmpeg_extract_subclip(
        video_s[1],
        start_time,
        end_time,
        targetname="assets/mp4/clip.mp4",
    )
    print_substep("Background video chopped successfully! 🎉", style="bold green")
