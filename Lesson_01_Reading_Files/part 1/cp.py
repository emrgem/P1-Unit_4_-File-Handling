file_path = 'programming_languages.txt'
#Open the file in read mode
with open(file_path,'r') as file:
    #1.Reading the entire text file content
    content = file.read()
    # print(file)
    # print(type(content))
    # print(content).
    
    #2.Reading line by line
    # file.seek(0)
    # content = file.readline()
    # print(content)
    
    file.seek(0)
    for line in file:
        print(line)
        break
    
    file.seek(0)
    #3.Reading all lines as a list
    lines = file.readlines()
    print(type(lines))
    print(lines)
    print(len(lines))
    
    #4 Reading a specific number of characters
    file.seek(0)
    partial_content = file.read(13)
    print(partial_content)
    partial_content = file.read(13)
    print(partial_content)
    file.seek(90)
    partial_content = file.read(13)
    print(partial_content)
    
    
