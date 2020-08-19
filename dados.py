import csv

with open('crono_2020.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')
    for x in leitor:
        print(f'{x[0]} data do resultado {x[16]}')
