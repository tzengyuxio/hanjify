import csv
import os
import deepl
from dotenv import load_dotenv
import shutil

def process_words(filename):
    # 創建備份文件
    backup_filename = f"{os.path.splitext(filename)[0]}_backup-words{os.path.splitext(filename)[1]}"
    shutil.copy2(filename, backup_filename)
    print(f"已創建備份文件: {backup_filename}")

    # 讀取已存在的CSV文件內容
    existing_words = set()
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # 確保行不為空
                    existing_words.add(row[0])
    except FileNotFoundError:
        # 如果文件不存在,就創建一個空集合
        pass

    header_size = 0 
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        header_size = len(header)
        print(f"header_size: {header_size}")

    # 讀取words.txt並處理每個單詞
    with open('words.txt', 'r', encoding='utf-8') as wordfile, \
         open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for word in wordfile:
            word = word.strip()  # 移除前後的空白字符
            if word and word not in existing_words:
                writer.writerow([word] + [''] * (header_size - 1))
                existing_words.add(word)  # 將新添加的單詞加入集合中

def translate_empty_fields(filename):
    # 創建備份文件
    backup_filename = f"{os.path.splitext(filename)[0]}_backup-trans{os.path.splitext(filename)[1]}"
    shutil.copy2(filename, backup_filename)
    print(f"已創建備份文件: {backup_filename}")

    # 初始化 DeepL 翻譯器
    load_dotenv()
    auth_key = os.getenv("DEEPL_AUTH_KEY")
    translator = deepl.Translator(auth_key)

    # 讀取並更新 CSV 文件
    rows = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 讀取標題行
        rows.append(header)

        # 找出 'chinese' 和 'japanese' 列的索引
        chinese_index = header.index('chinese') if 'chinese' in header else -1
        japanese_index = header.index('japanese') if 'japanese' in header else -1

        for row in reader:
            if chinese_index != -1 and japanese_index != -1:
                english = row[0]  # 假設英文總是在第一列
                chinese = row[chinese_index]
                japanese = row[japanese_index]

                # 如果中文欄位為空，翻譯成中文
                if not chinese.strip():
                    try:
                        chinese = translator.translate_text(english, target_lang="ZH-HANT").text
                        row[chinese_index] = chinese
                        print(f"翻譯 '{english}' 到中文: {chinese}")
                    except Exception as e:
                        print(f"翻譯 '{english}' 到中文時出錯: {e}")

                # 如果日文欄位為空，翻譯成日文
                if not japanese.strip():
                    try:
                        japanese = translator.translate_text(english, target_lang="JA").text
                        row[japanese_index] = japanese
                        print(f"翻譯 '{english}' 到日文: {japanese}")
                    except Exception as e:
                        print(f"翻譯 '{english}' 到日文時出錯: {e}")

            rows.append(row)  # 保留原始行的所有其他數據

    # 將更新後的內容寫回 CSV 文件
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

if __name__ == '__main__':
    filename = 'hanjify_translated.csv'

    process_words(filename)
    print("處理完成。新單詞已添加到hanjify_translated.csv文件中。")
    
    translate_empty_fields(filename)
    print("翻譯完成。空白欄位已更新。")
