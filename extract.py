import csv
import json
import os
import shutil


def convert_csv_to_js(input_file, output_file):
    # Read CSV file
    with open(input_file, "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        data = {}
        for row in reader:
            word, hanzi = row["word"], row["hanzi"]
            if hanzi != "" and hanzi != "-":
                counter += 1
                print(f"[{counter}] '{word}' -> '{hanzi}'...")
                data[word] = hanzi

    # Backup existing file if it exists
    if os.path.exists(output_file):
        backup_file = output_file.replace('.js', '_backup.js')
        shutil.copy2(output_file, backup_file)
        print(f"Existing file backed up as {backup_file}")

    # Save to JavaScript file
    with open(output_file, "w", encoding='utf-8') as jsfile:
        jsfile.write("const wordList = ")
        json.dump(data, jsfile, ensure_ascii=False, indent=2)
        jsfile.write(";")

    print(f"Total words: {counter}")
    print(f"Data has been written to {output_file}")


if __name__ == "__main__":
    csv_file = "hanjify_translated.csv"
    js_file = "wordlist.js"
    convert_csv_to_js(csv_file, js_file)
