# from deep_translator import GoogleTranslator
# import csv
# path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\Part 1 - Reading & Writing\\practice 2\\'
# txtFile = 'just_spanish.txt'
# csvFile = 'translated.csv'
# with open(path+txtFile,'r') as file:
#     with open(path+csvFile,'w') as newFile:
#     #    words = file.readlines()
#         writer = csv.writer(newFile)
#         writer.writerow(['Spanish','English','French','German'])
#         for spanish_word in file:
#             spanish_word = spanish_word.strip()
#             # print(word)
#             english = GoogleTranslator(source='auto', target='en').translate(spanish_word)
#             french = GoogleTranslator(source='auto', target='fr').translate(spanish_word)
#             german = GoogleTranslator(source='auto', target='de').translate(spanish_word)
#             writer.writerow([spanish_word,english,french,german])
#         print('All translated!')
        
# from deep_translator import GoogleTranslator
# import csv
# path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\Part 1 - Reading & Writing\\practice 2\\'
# txtFile = 'just_spanish.txt'
# csvFile = 'translated.csv'
# with open(path+txtFile,'r') as file:
#     with open(path+csvFile,'w') as newFile:
#     #    words = file.readlines()
#         writer = csv.writer(newFile)
#         writer.writerow(['Spanish','English','French','German'])
#         spanish = [line.strip() for line in file]
#         english = GoogleTranslator(source='auto', target='en').translate(spanish)
#         french = GoogleTranslator(source='auto', target='fr').translate(spanish)
#         german = GoogleTranslator(source='auto', target='de').translate(spanish)
#         zipped = zip(spanish,english,french,german)
#         writer.writerows(zipped)
#         print('All translated!')
    
from deep_translator import GoogleTranslator
import csv

path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\Part 1 - Reading & Writing\\practice 2\\'
txtFile = 'just_spanish.txt'
csvFile = 'translated.csv'

with open(path + txtFile, 'r') as file:
    spanish_words = [line.strip() for line in file]
    
    # # Translate all Spanish words in batches
    english_translations = GoogleTranslator(source='auto', target='en').translate_batch(spanish_words)
    french_translations = GoogleTranslator(source='auto', target='fr').translate_batch(spanish_words)
    german_translations = GoogleTranslator(source='auto', target='de').translate_batch(spanish_words)
    
    # Collect translations in a list of lists
    translations = [['Spanish', 'English', 'French', 'German']]
    for spanish, english, french, german in zip(spanish_words, english_translations, french_translations, german_translations):
        translations.append([spanish, english, french, german])

# Write all translations to CSV using writerows()
with open(path + csvFile, 'w', newline='', encoding='utf-8') as newFile:
    writer = csv.writer(newFile)
    writer.writerows(translations)

print('All translated!')
