import re
import logger

def delete():
    with open ('students_info.csv', 'r', encoding='utf-8', newline='') as file:
        lst = file.readlines()
        id = input('Введите ID: ')
        pattern = re.compile(re.escape(id))
        with open('students_info.csv', 'w', encoding='utf-8', newline='') as f:
            for i in lst:
                result = pattern.search(i)
                if result is None:
                    f.write(i)
    logger.info_logger(f'Удаление записи: {pattern}')










