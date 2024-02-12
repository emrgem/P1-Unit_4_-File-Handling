from deep_translator import GoogleTranslator
import csv
import time
path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\Part 1 - Reading & Writing\\practice 2\\'
txtFile = 'just_spanish.txt'
csvFile = 'translated.csv'
with open(path+txtFile,'r') as file:
    spanish_words = [line.strip() for line in file]
    #translate all spanish words in batches
    start_translation = time.time()
    english = GoogleTranslator(source='auto', target='en').translate_batch(spanish_words)
    french = GoogleTranslator(source='auto', target='fr').translate_batch(spanish_words)
    german = GoogleTranslator(source='auto', target='de').translate_batch(spanish_words)
    end_translation = time.time()
    translation_execution = end_translation - start_translation
    print(f"Translation Time:{translation_execution} seconds")
    
    final_translations = [['Spanish','English','French','German']]
    for es, en, fr, de in zip(spanish_words, english, french, german):
        final_translations.append([es, en, fr, de])
    start_writing = time.time()
    with open(path+csvFile, 'w', newline='') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(final_translations)
    end_writing = time.time()
    writing_execution = end_writing - start_writing
    print(f"Writing Time: {writing_execution} seconds")
        