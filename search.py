import csv

def search():
    a = input('Введите данные для поиска: ')
    with open ('students_info.csv', encoding='utf-8', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')   
        for row in csv_reader:
            for field in row:
                if field == a:
                    print(row[0], row[1], row[2], row[3], row[4], row[5])   