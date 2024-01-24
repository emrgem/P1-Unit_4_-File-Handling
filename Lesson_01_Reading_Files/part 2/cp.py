file_path = "Lesson_01_Reading_Files\part 2\quotes.txt"
with open(file_path,'r') as file:
    '''
    for line in file:
        # print(line)
        print(line.rstrip())
    '''
    '''
    while True:
        line = file.readline()
        if not line:
            break
        # print(line)
        print(line.rstrip()) #rstrip() removes trailing whitespace
    '''
    '''
    # Reading and Processing Lines with enumerate:
    for line_number,line_content in enumerate(file,1):
        print(f"Line {line_number}: {line_content.strip()}")
    '''
    # Reading a specific number of lines
    num_lines_to_read = 3
    for _ in range(num_lines_to_read):
        line = file.readline()
        print(line.strip())