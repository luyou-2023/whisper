import whisper
import os
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# os.environ["HF_HOME"] = "/Users/luyou/code_work/shopastro/rust_code/whisper/data"

os.environ["PATH"] += os.pathsep + "/System/Volumes/Data/Users/luyou/Library/Application Support/bilibili/ffmpeg"
# os.environ["WHISPER_FFMPEG_PATH"] = "/System/Volumes/Data/Users/luyou/Library/Application Support/bilibili/ffmpeg/ffmpeg"
#/Users/luyou/.cache/whisper/medium.pt
model = whisper.load_model("medium")

print(model)


result = model.transcribe("jfk.flac", verbose=True)
print(result)

# Base Model
# Detected language: Italian
# [00:00.000 --> 00:07.160]  Ciao! Il mio nome è Marco e vivo all'ondro.
# [00:07.160 --> 00:11.400]  E tu chi sei?

# Medium Model
# Detected language: Italian
# [00:00.000 --> 00:09.600]  Ciao, il mio nome è Marco e vivo a Londra. E tu chi sei?
