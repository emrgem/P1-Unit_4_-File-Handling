import csv
file_path = 'P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\roster.csv'
with open(file_path,newline='') as file:
    with open('P1-Unit_4_-File-Handling\\Lesson_04_CSV_FILES\\names.csv', 'w', newline='') as newFile:        
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        writer = csv.writer(newFile)
        writer.writerow(['First Name', 'Last Name'])
        for row in data:
            # writer.writerow([row[1].split(', ')[1],row[1].split(', ')[0]])
            last,first = row[1].split(', ')
            writer.writerow([first,last])
    
data =[]
for row in reader:
    data.append(row)
    print(data)
