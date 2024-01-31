# from deep_translator import GoogleTranslator
# text = 'happy coding'
# translated = GoogleTranslator(source='auto', target='es').translate(text=text)
# translated = GoogleTranslator(source='auto', target='tr').translate_file("Lesson_03_API\\part1\\spanish_words.txt")
# print(translated.encode("utf-8"))

# #1 read the file line by line
# from deep_translator import GoogleTranslator
# with open("Lesson_03_API\\part1\\spanish_words.txt","r") as myfile:
#     for word in myfile:
#         # print(word)
#         # remove the newline character \n
#         word = word.strip()
#         # print(word)
#         # translate word from spanish to english
#         translated = GoogleTranslator(source="auto",target="en").translate(word)
#         full = f"{word}: {translated}"
#         print(full)

# store each word as a key in dictionary and then translate the entire file
from deep_translator import GoogleTranslator
# create a dict to store words
word_dict = {}
with open("Lesson_03_API\\part1\\spanish_words.txt","r") as myfile:
    for word in myfile:
        word = word.strip()
        word_dict[word] = None #placeholder for the translation
# print(word_dict)
# translate the entire file(the dictionary)
translated_text = GoogleTranslator(source="auto", target="en").translate(' '.join(word_dict.keys()))

# split the translated text back into words
translated_words = translated_text.split()

# populate the dictionary with the translations
for word,translation in zip(word_dict.keys(),translated_words):
    word_dict[word] = translation

# for word, translation in word_dict.items():
#     print(f"{word}:{translation}")

# # 1 write the translation via write()
# with open("Lesson_03_API\\part1\\es_en_translated.txt", "w") as output_file:
#     for word, translation in word_dict.items():
#         output_file.write(f"{word}:{translation}\n")

# 2 write the translation via writelines()
with open("Lesson_03_API\\part1\\es_en_translated2.txt", "w") as output_file:
    output_file.writelines([f"{word}:{translation}\n" for word,translation in word_dict.items()])