import json, csv
path = "P1-Unit_4_-File-Handling\\Lesson_05_JSON_FILES\\Part 2 - JSON to CSV\\"
with open(path+"dunkinDonuts.json") as file:
    data = json.load(file)
    data = data['data']
# fieldnames = ['address', 'city', 'state', 'country','lat', 'lng', 'phonenumber' ]

with open(path+'dunkinDonuts.csv', 'w', newline='', encoding='utf-8') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=data[0].keys())
   
    # Write the header to the CSV file
    writer.writeheader()
   
    # Write the data to the CSV file
    writer.writerows(data)
