def get_student ():
    info = []
    id = input('Введите ID:')
    info.append(id)
    surname = input('Введите фамилию: ')
    info.append(surname)
    name = input('Введите имя: ')
    info.append(name)
    birthday = input('Введите дату рождения: ')
    info.append(birthday)
    school_class = input('Введите номер класса: ')
    info.append(school_class)
    description = input('Введите описание: ')
    info.append(description)
    return info