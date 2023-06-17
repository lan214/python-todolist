import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

station = input("Enter the city: ")

for row in data[1:]:
    if row[0] == station:
        print(row[1])