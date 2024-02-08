import csv
file_path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\roster.csv'
with open(file_path,newline='') as file:
    reader = csv.reader(file)
    # print(type(reader))
    # for row in reader:
        # print(row[1]) 
        # print(row)
    # get the header row
    header = next(reader)
    # print(header)
    
    #Read the remaining data
    # for row in reader:
    #     print(row)
    
    # convert reader into a list
    data = [row for row in reader]
    
with open('P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\names.csv','w', newline='') as newFile:
    writer = csv.writer(newFile)
    writer.writerow(['First Name','Last Name'])