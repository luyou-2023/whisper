import whisper
from pytube import YouTube
import urllib.request
os.environ["HTTPS_PROXY"] = "https://127.0.0.1:7890"
model = whisper.load_model("medium")
headers = {"User-Agent": "Mozilla/5.0"}
opener = urllib.request.build_opener()
opener.addheaders = [(key, value) for key, value in headers.items()]
urllib.request.install_opener(opener)

#Download a video from Youtube, get audio track 1 and transcribe
youtube_video_url = "https://www.youtube.com/watch?v=4IW-OuV3IH4"
youtube_video_content = YouTube(youtube_video_url)

audio_streams = youtube_video_content.streams.filter(only_audio=True)
audio_stream = audio_streams[1]
audio_stream.download("")

model = whisper.load_model("base")
result = model.transcribe(str(audio_stream.default_filename), verbose=True)
print(result)
