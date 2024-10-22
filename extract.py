import csv
import json


def convert_csv_to_json(input_file, output_file):
    # Read CSV file
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        data = {}
        for row in reader:
            word, hanzi = row["word"], row["hanzi"]
            if hanzi != "" and hanzi != "-":
                counter += 1
                print(f"[{counter}] '{word}' -> '{hanzi}'...")
                data[word] = hanzi

    # Save to JSON file
    with open(output_file, "w") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)

    print(f"Total words: {counter}")


if __name__ == "__main__":
    csv_file = "hanjify_translated.csv"
    json_file = "word_list.json"
    convert_csv_to_json(csv_file, json_file)
