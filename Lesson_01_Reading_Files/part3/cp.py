file_path = "apcsp_vocab.txt"
with open(file_path,'r') as file:
    content = file.readlines() # we got a list of lines
    # print(content)
    #Extract the words and remove the duplicates
    words = list({line[:line.find(':')] for line in content})
    sorted_words = sorted(words)
    # print(sorted_words)
    for word in sorted_words:
        print(word)