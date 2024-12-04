from django.test import TestCase

# Create your tests here.

import requests

url = "http://127.0.0.1:8000/video-lessons/flag-trend.mp4"
files = {
    'title': (None, 'example_video'),
    'video_file': open('flag-trend.mp4', 'rb'),
}
response = requests.post(url, files=files)
print(response.json())
