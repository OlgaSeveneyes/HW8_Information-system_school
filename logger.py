from datetime import datetime as dt
import logging

def info_logger(info):
    time = dt.now().strftime('%D_%H:%M')
    with open ('students_info_logger.csv', 'a', encoding="utf-8") as file:
        file.write('{};phonebook;{}\n'
                    .format(time, info))

logging.basicConfig(
    level=logging.INFO,
    filename='students_info_logger.csv',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
