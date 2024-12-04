import whisper
import os
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# os.environ["HF_HOME"] = "/Users/luyou/code_work/shopastro/rust_code/whisper/data"

os.environ["PATH"] += os.pathsep + "/System/Volumes/Data/Users/luyou/Library/Application Support/bilibili/ffmpeg"
# os.environ["WHISPER_FFMPEG_PATH"] = "/System/Volumes/Data/Users/luyou/Library/Application Support/bilibili/ffmpeg/ffmpeg"
#/Users/luyou/.cache/whisper/medium.pt
model = whisper.load_model("medium")

print(model)

'''
sample = {
    "input_features": [
        [-12.3, -10.5, -8.7, ..., -15.1],  # 第一帧的 80 个频率特征
        [-11.2, -9.8, -7.6, ..., -14.0],  # 第二帧的 80 个频率特征
        ...,
        [-13.5, -11.4, -9.2, ..., -16.8]  # 第100帧的 80 个频率特征
    ],  
    "labels": [8, 5, 12, 12, 15, 27, 23, 15, 18, 12, 4]  # 对应文本序列标签
}

char_to_int = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27
}
'''

result = model.transcribe("jfk.flac", verbose=True)
print(result)

# Base Model
# Detected language: Italian
# [00:00.000 --> 00:07.160]  Ciao! Il mio nome è Marco e vivo all'ondro.
# [00:07.160 --> 00:11.400]  E tu chi sei?

# Medium Model
# Detected language: Italian
# [00:00.000 --> 00:09.600]  Ciao, il mio nome è Marco e vivo a Londra. E tu chi sei?
