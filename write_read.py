import csv
import get_info
import logger

# записали введенные данные в файл

def write_file():
    new_record = get_info.get_student()
    with open('students_info.csv', 'a', encoding='utf-8', newline='') as file:
        fieldnames = ['name', 'surname', 'date', 'school_class', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'name': new_record[0], 'surname': new_record[1], 'date': new_record[2], 'school_class': new_record[3], 'description': new_record[4]})
    logger.info_logger(f'Новая запись в тел.книгу 1: {new_record}')

# Считываем из файла 

def read_file():
    # with open ('students_info.csv', newline='') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         print(row['name'], row['surname'])
    # return(reader)

    with open ('students_info.csv', 'r', encoding='utf-8', newline='') as file:
        list = file.read()
        return(list)
        
print(type(read_file()))