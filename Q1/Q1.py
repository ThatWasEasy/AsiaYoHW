from collections import Counter
import re

with open("words.txt", 'r') as file:
    # 讀取檔案內容並轉換為小寫
    text = file.read().lower()
    # 移除標點符號，只保留單字，蠻有趣的，透過此次作業查詢資料才發現 python 有處理正則表達式的函式庫可用
    words = re.findall(r'\b[a-z]+\b', text)
    # 計算單字出現次數
    word_counts = Counter(words)
    # 找出出現次數最多的單字，Counter 的 .most_common 函式也是透過此次查詢才了解到
    most_common_word, count = word_counts.most_common(1)[0]
    print(count, most_common_word)
