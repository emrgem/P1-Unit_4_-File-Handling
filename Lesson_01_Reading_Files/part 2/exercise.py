file_path = "Lesson_01_Reading_Files\part 2\quotes.txt"
def printLine(path,target_line_number):
    try: #open the file, find the line, and print
        with open(path,'r') as file:
            for current_line_number, content in enumerate(file,1):
                if current_line_number == target_line_number:
                    print(f"Line {current_line_number}: {content.strip()}")
                    return
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
    except Exception as e:
        print(f"An error occured: {e}")

printLine(file_path,7)
# printLine("quotes.txt",7)