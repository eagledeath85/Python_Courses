import csv

csv_file = 'OlympicMedals_2020.csv'

with open(csv_file, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f"Column Headers: {headers}")
    reader = csv.reader(csv_file)
    for rank, country, gold, silver, bronze, total in reader:
            rank = int(rank)
            country = str(country)
            gold = int(gold)
            silver = int(silver)
            bronze = int(bronze)
            total = int(total)
            print(rank, country, gold, silver, bronze, total)