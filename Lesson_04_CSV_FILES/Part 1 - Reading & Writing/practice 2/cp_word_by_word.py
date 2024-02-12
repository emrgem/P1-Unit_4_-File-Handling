from deep_translator import GoogleTranslator
import csv
import time
path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\Part 1 - Reading & Writing\\practice 2\\'
txtFile = 'just_spanish.txt'
csvFile = 'translated.csv'
with open(path+txtFile,'r') as file:
    with open(path+csvFile,'w') as newFile:
    #    words = file.readlines()
        writer = csv.writer(newFile)
        writer.writerow(['Spanish','English','French','German'])
        translated = []
        start_translation_time = time.time()
        for spanish_word in file:
            spanish_word = spanish_word.strip()
            # print(word)
            english = GoogleTranslator(source='auto', target='en').translate(spanish_word)
            french = GoogleTranslator(source='auto', target='fr').translate(spanish_word)
            german = GoogleTranslator(source='auto', target='de').translate(spanish_word)
            # writer.writerow([spanish_word,english,french,german])
            translated.append([spanish_word,english,french,german])
        end_translation_time = time.time()
        translation_execution_time = end_translation_time - start_translation_time
        print(f"Translation Time:{translation_execution_time} seconds")
        
        start_writing_time = time.time()    
        writer.writerows(translated)
        end_writing_time = time.time()
        writing_execution_time = end_writing_time - start_writing_time
        print(f"Writing time: {writing_execution_time} seconds")
        
        print('All translated!')
        

