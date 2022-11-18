# from googletrans import Translator
# import base64
# import time
# translator = Translator()


# while True:
#     translated = input("Enter text to translate: ")
    
#     first = translated
#     language_list = [ 'es', 'fr', 'ja', 'ru', 'zh-CN', 'zh-TW', 'ar', 'de', 'it', 'ko', 'pt', 'tr', 'vi',
#                     'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW',
#                     'co', 'hr', 'cs', 'da', 'nl', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu',]
#     #Remove duplicates
#     language_list = list(dict.fromkeys(language_list))
#     amount_of_languages = int(input(f"How many languages do you want to translate to 1-{len(language_list)}? "))
#     #Make the list smaller according to the amount_of_languages
#     if amount_of_languages <= len(language_list):
#         language_list = language_list[:amount_of_languages]
#     else:
#         language_list = language_list[:4]

#     print("Started")
#     count = 0
#     for language in language_list:
#         count += 1
#         translated = translator.translate(translated, dest=language).text

#         finish = len(language_list)
#         percentage = (count / finish) * 100
#         print(f"{int(round(percentage))}% {language} -> {translated}")

#     finished = translator.translate(translated, dest='en').text

#     first_len = len(first)
#     finished_len = len(finished)
#     translated_times = len(language_list)
#     print(f"Original: {first} -> {first_len}")
#     print(f"Translated: {finished} -> {finished_len}")

#     print('\n\n\n')
#     print("Finished")


#     time.sleep(3)



#Basic flask app
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



app.run(debug=True)



