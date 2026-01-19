import json
import random
import requests
import os


PAGE_TOKEN = os.environ["PAGE_TOKEN"]
PAGE_ID = os.environ["PAGE_ID"]

AR_JSON_PATH = "surahs.json"
EN_JSON_PATH = "surahs_en.json"

def generate_random_ayah():
    with open(AR_JSON_PATH, "r", encoding="utf-8") as file:
        data_ar = json.load(file)

    with open(EN_JSON_PATH, "r", encoding="utf-8") as file:
        data_en = json.load(file)

    surahs_ar = data_ar["data"]["surahs"]
    surahs_en = data_en["data"]["surahs"]

    index = random.randrange(len(surahs_ar))
    random_surah_ar = surahs_ar[index]
    random_surah_en = surahs_en[index]

    ayah_index = random.randrange(len(random_surah_ar["ayahs"]))
    random_ayah_ar = random_surah_ar["ayahs"][ayah_index]
    random_ayah_en = random_surah_en["ayahs"][ayah_index]

    output_text = (
        f"{random_ayah_ar['text']}\n\n"
        f"{random_ayah_en['text']}\n\n"
        f"{random_surah_ar['name']} | ({random_surah_en['englishName']})\n"
        f"رقم الآية: {random_ayah_ar['numberInSurah']}\n"
    )

    return output_text

def post_to_facebook():
    ayah_text = generate_random_ayah()

    # النشر على الصفحة
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    data = {
        "message": ayah_text,
        "access_token": PAGE_TOKEN
    }
    response = requests.post(url, data=data)
    print(response.json())

if __name__ == "__main__":
    post_to_facebook()
