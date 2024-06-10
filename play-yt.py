import cv2
import numpy as np
from pytube import YouTube
from asciimatics.screen import Screen
from rich.console import Console
console = Console()

WIDTH = round(1280/(7))
HEIGHT = round(720/(16))
speed = 0.00000000000000000000005

ASCII_CHARS = "  ░░▒▒▓▓██"

def __get_video_stream_url__(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    return stream.url

def __video_to_ascii__(cap):
    ret, frame = cap.read()
    if not ret:
        return None

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    small_frame = cv2.resize(gray_frame, (WIDTH, HEIGHT))
    ascii_frame = np.zeros(small_frame.shape, dtype=str)

    for i in range(small_frame.shape[0]):
        for j in range(small_frame.shape[1]):
            pixel_value = small_frame[i, j]
            ascii_char = ASCII_CHARS[pixel_value // 32]  # Use 32 to map 256 values to 8 characters
            ascii_frame[i, j] = ascii_char

    frame_str = "\n".join("".join(row) for row in ascii_frame)
    return frame_str

def __play_ascii_video__(screen, video_url):
    cap = cv2.VideoCapture(__get_video_stream_url__(video_url))
    
    while cap.isOpened():
        frame = __video_to_ascii__(cap)
        if frame is None:
            break
        screen.clear()
        for y, line in enumerate(frame.split('\n')):
            screen.print_at(line, 0, y)
        screen.refresh()
        screen.wait_for_input(speed)  # Adjust the speed as necessary

    cap.release()

def main(video_url):
    Screen.wrapper(__play_ascii_video__, arguments=['https://www.youtube.com/watch?v='+video_url])
