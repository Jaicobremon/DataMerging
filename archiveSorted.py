import csv

data = []
with open("archive_dataset.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)
headers = data[0]
planet_data = data[1:]

for dataPoint in planet_data:
    dataPoint[0] = dataPoint[0].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])

with open("archive_dataset.csv","a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)

with open("archive_dataset.csv") as input,open("archive_dataset1.csv","w",newline = "") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row) 