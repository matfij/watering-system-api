import csv
import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('data_file', type=str)
args = parser.parse_args()

url = 'http://127.0.0.1:8000/api/humidity/'
plant_id = 1
data_file = 'api/tools/data/' + args.data_file

with open(data_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        date = row[0] + ' ' + row[1][:row[1].rindex(';')]
        value = row[1][row[1].rindex(';')+1:].replace(',', '.')

        body = {
            'plant_id': plant_id,
            'value': str(value),
            'date': str(date)
        }

        r = requests.post(url, data=body)
