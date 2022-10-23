import search
import write_read
import delete
import change

def menu():
    m = input('''База данных школы №3.
            \nВведите 1 для поиска ученика:  
            \nВведите 2 для создания новой записи: 
            \nВведите 3 для удаления записи:  
            \nВведите 4 для изменения записи: 
            \nВведите 5 для отображения базы данных на экране:
            \nВведите 0 для выхода: \n''')

    match m:
        case '1':
            return search.search()
        case '2':
            return write_read.write_file()
        case '3':
            return delete.delete()    
        case '4':
            return change.change()
        case '5':
            return write_read.read_file()
        case '0':
            return