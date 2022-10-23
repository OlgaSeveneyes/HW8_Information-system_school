import csv
import get_info
import logger

# записали введенные данные в файл

def write_file():
    new_record = get_info.get_student()
    fieldnames = ['ID','name', 'surname', 'date', 'school_class', 'description']
    with open('students_info.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter= ',', lineterminator="\r")
        #writer.writeheader()
        writer.writerow({'ID': new_record[0], 'name': new_record[1], 'surname': new_record[2], 'date': new_record[3], 'school_class': new_record[4], 'description': new_record[5]})
    logger.info_logger(f'Новая запись в тел.книгу 1: {new_record}')

# Считываем и печатаем данные из файла 
        
def read_file():
    with open ('students_info.csv', 'r', encoding='utf-8', newline='') as file:
        list = file.read()
        some_list = list.replace(','," ")
    print(some_list)

