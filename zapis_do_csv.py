import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('plik.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    csvwriter.writeheader()

    for row in data:
        list=row['rates']
    
    for x in list:
        csvwriter.writerow(x)