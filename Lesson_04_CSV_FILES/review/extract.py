import csv
folder_path = "P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\review\\"
def extract_columns(file_path):
    with open(file_path, newline="") as input_file:
        reader = csv.reader(input_file)
        #Get the header row
        header = next(reader)
        #Print the columns in the given file
        print("Columns in the given file:")
        # print(header)
        for index, val in enumerate(header):
            print(f"{index} : {val}")
        column_numbers = input('Enter column numbers separated by space:').split()
        column_numbers = [int(i) for i in column_numbers]
        selected_columns = [header[i] for i in column_numbers]
        print(f"You selected column(s):{selected_columns}")
        #create a new csv file to write selected columns
        with open(folder_path+"new_file.csv",'w',newline="") as output_file:
            writer = csv.writer(output_file)
            #write the selected columns
            writer.writerow(selected_columns)
            #Extract data from the input file based on the selected columns
            data = [[row[i] for i in column_numbers] for row in reader]
            # print(data)
            writer.writerows(data)
            print(f"{len(selected_columns)} column(s) extracted!")
        

extract_columns(folder_path + "roster.csv")