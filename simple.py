import csv
import os

import deepl
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def convert_to_list(obj, key_order):
    return [obj.get(key, "") for key in key_order]


def load_wordlist_from_csv(file_path):
    # load csv file and convert to a dict with word and object, the object is a dict zip with header and row value
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = {}
        for row in reader:
            key = row[0]
            value = dict(zip(headers, row))
            if key in data:
                print(
                    f"Info: Key collision detected for key '{key}'. Overwriting existing value."
                )
            data[key] = value
        return data


def save_wordlist_to_csv(wordlist, file_path):
    # Extract header from any value of the data
    header = list(next(iter(wordlist.values())).keys())

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header row

        # Write data rows
        for value in wordlist.values():
            row = list(value.values())
            writer.writerow(row)


def fetch_basic_english_wordlist(url, output_csv, api_key):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")
    words = []

    for paragraph in paragraphs:
        first_child = paragraph.find()
        if (
            first_child
            and first_child.name == "b"
            and first_child.text
            in ["Basic:", "International:", "Addendum:", "Compound:", "Endings:"]
        ):
            source = first_child.text.strip(":")
            all_words = paragraph.text[paragraph.text.find(":") + 1 :].split(" • ")
            for word in all_words:
                word = word.strip()
                print(word)
                hanzi = "-" if len(word) <= 3 else ""
                words.append([word, source, "", hanzi, ""])

    if not words:
        print("Error: No words found in the word list.")
        return

    # translator = deepl.Translator(api_key)

    # Translate words to Chinese
    # for row in words:
    #     try:
    #         translated_text = translator.translate_text(row[0], target_lang="ZH-TW")
    #         row[2] = translated_text.text
    #     except Exception as e:
    #         print(f"Error translating word '{row[0]}': {e}")

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["word", "source", "chinese", "hanzi", "memo"])
        writer.writerows(words)

    print(f"CSV file '{output_csv}' has been successfully created.")


def fetch_be850_wordlist(input_wordlist, output_csv):
    be850_wordlists = {
        "operations": "come, get, give, go, keep, let, make, put, seem, take, be, do, have, say, see, send, may, will, about, across, after, against, among, at, before, between, by, down, from, in, off, on, over, through, to, under, up, with, as, for, of, till, than, a, the, all, any, every, no, other, some, such, that, this, I, he, you, who, and, because, but, or, if, though, while, how, when, where, why, again, ever, far, forward, here, near, now, out, still, then, there, together, well, almost, enough, even, little, much, not, only, quite, so, very, tomorrow, yesterday, north, south, east, west, please, yes",
        "general": "account, act, addition, adjustment, advertisement, agreement, air, amount, amusement, animal, answer, apparatus, approval, argument, art, attack, attempt, attention, attraction, authority, back, balance, base, behaviour, belief, birth, bit, bite, blood, blow, body, brass, bread, breath, brother, building, burn, burst, business, butter, canvas, care, cause, chalk, chance, change, cloth, coal, colour, comfort, committee, company, comparison, competition, condition, connection, control, cook, copper, copy, cork, cotton, cough, country, cover, crack, credit, crime, crush, cry, current, curve, damage, danger, daughter, day, death, debt, decision, degree, design, desire, destruction, detail, development, digestion, direction, discovery, discussion, disease, disgust, distance, distribution, division, doubt, drink, driving, dust, earth, edge, education, effect, end, error, event, example, exchange, existence, expansion, experience, expert, fact, fall, family, father, fear, feeling, fiction, field, fight, fire, flame, flight, flower, fold, food, force, form, friend, front, fruit"
        + ","
        + "glass, gold, government, grain, grass, grip, group, growth, guide, harbour, harmony, hate, hearing, heat, help, history, hole, hope, hour, humour, ice, idea, impulse, increase, industry, ink, insect, instrument, insurance, interest, invention, iron, jelly, join, journey, judge, jump, kick, kiss, knowledge, land, language, laugh, law, lead, learning, leather, letter, level, lift, light, limit, linen, liquid, list, look, loss, love, machine, man, manager, mark, market, mass, meal, measure, meat, meeting, memory, metal, middle, milk, mind, mine, minute, mist, money, month, morning, mother, motion, mountain, move, music, name, nation, need, news, night, noise, note, number, observation, offer, oil, operation, opinion, order, organization, ornament, owner"
        + ","
        + "page, pain, paint, paper, part, paste, payment, peace, person, place, plant, play, pleasure, point, poison, polish, porter, position, powder, power, price, print, process, produce, profit, property, prose, protest, pull, punishment, purpose, push, quality, question, rain, range, rate, ray, reaction, reading, reason, record, regret, relation, religion, representative, request, respect, rest, reward, rhythm, rice, river, road, roll, room, rub, rule, run, salt, sand, scale, science, sea, seat, secretary, selection, self, sense, servant, sex, shade, shake, shame, shock, side, sign, silk, silver, sister, size, sky, sleep, slip, slope, smash, smell, smile, smoke, sneeze, snow, soap, society, son, song, sort, sound, soup, space, stage, start, statement, steam, steel, step, stitch, stone, stop, story, stretch, structure, substance, sugar, suggestion, summer, support, surprise, swim, system, talk, taste, tax, teaching, tendency, test, theory, thing, thought, thunder, time, tin, top, touch, trade, transport, trick, trouble, turn, twist, unit, use, value, verse, vessel, view, voice, walk, war, wash, waste, water, wave, wax, way, weather, week, weight, wind, wine, winter, woman, wood, wool, word, work, wound, writing, year",
        "things": "angle, ant, apple, arch, arm, army, baby, bag, ball, band, basin, basket, bath, bed, bee, bell, berry, bird, blade, board, boat, bone, book, boot, bottle, box, boy, brain, brake, branch, brick, bridge, brush, bucket, bulb, button, cake, camera, card, cart, carriage, cat, chain, cheese, chest, chin, church, circle, clock, cloud, coat, collar, comb, cord, cow, cup, curtain, cushion, dog, door, drain, drawer, dress, drop, ear, egg, engine, eye, face, farm, feather, finger, fish, flag, floor, fly, foot, fork, fowl, frame, garden, girl, glove, goat, gun, hair, hammer, hand, hat, head, heart, hook, horn, horse, hospital, house, island, jewel, kettle, key, knee, knife, knot, leaf, leg, library, line, lip, lock, map, match, monkey, moon, mouth, muscle, nail, neck, needle, nerve, net, nose, nut, office, orange, oven, parcel, pen, pencil, picture, pig, pin, pipe, plane, plate, plough, pocket, pot, potato, prison, pump, rail, rat, receipt, ring, rod, roof, root, sail, school, scissors, screw, seed, sheep, shelf, ship, shirt, shoe, skin, skirt, snake, sock, spade, sponge, spoon, spring, square, stamp, star, station, stem, stick, stocking, stomach, store, street, sun, table, tail, thread, throat, thumb, ticket, toe, tongue, tooth, town, train, tray, tree, trousers, umbrella, wall, watch, wheel, whip, whistle, window, wing, wire, worm",
        "qualities": "able, acid, angry, automatic, beautiful, black, boiling, bright, broken, brown, cheap, chemical, chief, clean, clear, common, complex, conscious, cut, deep, dependent, early, elastic, electric, equal, fat, fertile, first, fixed, flat, free, frequent, full, general, good, great, grey, hanging, happy, hard, healthy, high, hollow, important, kind, like, living, long, male, married, material, medical, military, natural, necessary, new, normal, open, parallel, past, physical, political, poor, possible, present, private, probable, quick, quiet, ready, red, regular, responsible, right, round, same, second, separate, serious, sharp, smooth, sticky, stiff, straight, strong, sudden, sweet, tall, thick, tight, tired, true, violent, waiting, warm, wet, wide, wise, yellow, young",
        "opposites": "awake, bad, bent, bitter, blue, certain, cold, complete, cruel, dark, dead, dear, delicate, different, dirty, dry, false, feeble, female, foolish, future, green, ill, last, late, left, loose, loud, low, mixed, narrow, old, opposite, public, rough, sad, safe, secret, short, shut, simple, slow, small, soft, solid, special, strange, thin, white, wrong",
    }

    header = list(next(iter(wordlist.values())).keys())
    header_be850 = "be850"
    # insert header_be850 to -3 position of header
    header.insert(-3, header_be850)

    for key, value in be850_wordlists.items():
        words = [w.strip() for w in value.split(",")]
        for word in words:
            if word in input_wordlist:
                input_wordlist[word][header_be850] = key
            else:
                input_wordlist[word] = {"word": word, header_be850: key}

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for word_data in input_wordlist.values():
            row = convert_to_list(word_data, header)
            writer.writerow(row)

    print(f"CSV file '{output_csv}' has been successfully created.")


def fetch_frequency_list_wikipedia_2016(wordlist, output_csv):
    header = list(next(iter(wordlist.values())).keys())
    header_wiki2016 = "wiki2016"
    header.insert(-3, header_wiki2016)

    url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    h2s = soup.find_all("h2")
    for h2 in h2s:
        if h2.text[-4:] in ["1000", "2000", "3000"]:
            source = "top %s" % h2.text[-4:]
            # get the next element of h2.parent
            frequency_paragraph = h2.parent.find_next_sibling()
            for a_tag in frequency_paragraph.find_all("a"):
                if a_tag.has_attr("class") and "new" in a_tag["class"]:
                    continue
                word = a_tag.text.strip()
                if word in wordlist:
                    wordlist[word][header_wiki2016] = source
                else:
                    wordlist[word] = {"word": word, header_wiki2016: source}

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for word_data in wordlist.values():
            row = convert_to_list(word_data, header)
            writer.writerow(row)

    print(f"CSV file '{output_csv}' has been successfully created.")


def translate_wordlist(wordlist, output_csv, api_key):
    translator = deepl.Translator(api_key)
    translate_count = 0

    header = list(next(iter(wordlist.values())).keys())
    field = "japanese"  # "chinese"

    for word_data in wordlist.values():
        word = word_data["word"]
        if field in word_data and word_data[field]:
            continue
        translate_count += 1
        print(f"[{translate_count}] Translating '{word}'...")
        # translation = translator.translate_text(word, target_lang="ZH-HANT")
        try:
            translation = translator.translate_text(word, target_lang="JA")
        except deepl.exceptions.DeepLException as e:
            print(f"-- Error translating '{word}': {e}")
            continue
        word_data[field] = translation

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for word_data in wordlist.values():
            row = convert_to_list(word_data, header)
            writer.writerow(row)


load_dotenv()
url = "https://simple.wikipedia.org/wiki/Wikipedia:Basic_English_combined_wordlist"
output_csv = "basic_english_wordlist.csv"
api_key = os.getenv("DEEPL_AUTH_KEY")

# fetch_basic_english_wordlist(url, output_csv, api_key)

# wordlist = load_wordlist_from_csv(output_csv)
output_csv = "with_be850_wordlist.csv"
# fetch_be850_wordlist(wordlist, output_csv)

# wordlist = load_wordlist_from_csv(output_csv)
# output_csv = "with_wiki2016_wordlist.csv"
# fetch_frequency_list_wikipedia_2016(wordlist, output_csv)

wordlist = load_wordlist_from_csv("hanjify_cj.csv")
output_csv = "hanjify_translated.csv"
translate_wordlist(wordlist, output_csv, api_key)


# NOTES:
#
# wordlists:
# - Basic English (850 word roots) https://en.wikipedia.org/wiki/Basic_English
#   - 只有 18 個動詞
# - https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)
#
# some rules (參考 basic english)
# - 複數添加 "-s" (不管原本是 -s or -es or -ies)
# - 名詞添加 "-er" 或 "-ing"
# - 副詞添加 "-ly"
# - 否定添加 "un-"
