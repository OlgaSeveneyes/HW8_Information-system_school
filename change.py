import re
import logger
import write_read


def change():

    with open ('students_info.csv', 'r', encoding='utf-8', newline='') as file:
        lst = file.readlines()
        id = input('Введите ID ученика для изменения данных: ')
        pattern = re.compile(re.escape(id))
        with open('students_info.csv', 'w', encoding='utf-8', newline='') as f:
            for i in lst:
                result = pattern.search(i)
                if result is None:
                    f.write(i)
    print('Введите новые данные: ')
    file = write_read.write_file()
    logger.info_logger(f'Изменение записи: {pattern}')

