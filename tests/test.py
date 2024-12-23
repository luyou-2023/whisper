import numpy as np

# 假设音频的特征数据 (Mel频谱图)
input_features = [
    [-12.3, -10.5, -8.7, -11.2, -10.8, -12.0, -13.1, -15.1],  # 第1帧
    [-11.2, -9.8, -7.6, -10.4, -9.5, -11.2, -13.0, -14.0],   # 第2帧
    [-10.5, -8.7, -6.9, -9.7, -8.4, -10.2, -12.5, -13.7],    # 第3帧
    # ... 继续添加更多帧
    [-13.5, -11.4, -9.2, -10.3, -9.9, -11.2, -14.3, -16.8]   # 第100帧
]

# 假设文本标签对应的数字
# 文本 "HELLO WORLD" 的数字编码
labels = [8, 5, 12, 12, 15, 27, 23, 15, 18, 12, 4]  # 例如：H -> 8, E -> 5, ...

# 字符到数字的映射 (示例)
char_to_int = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27
}

# 数字到字符的映射
int_to_char = {v: k for k, v in char_to_int.items()}

# 解码数字标签为文本
decoded_text = ''.join([int_to_char[label] for label in labels])

# 打印解码后的文本
print("Decoded Text:", decoded_text)

# 输出:
# Decoded Text: HELLO WORLD
