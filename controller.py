# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

import input_data
import prog
import out


def book():
    while True:
        print('Список команд: \n 1 - добавить контакт \n 2 - удалить контакт \n 3 - посмотреть список контактов \n 4 - найти номер по имени \n 5 - завершить работу \n')
        command = int(input('Введите номер команды: '))
        if command == 1:
            a = input_data.get_name()
            b = input_data.get_number()
            input_data.phone_number(a, b)
            book_new = input_data.get_data()
            prog.save_phone_number(book_new)
            print('Данные сохранены \n')
        elif command == 2:
            x = input_data.search_contact()
            prog.del_phone_number(x)
            print('Данные удалены \n')
        elif command == 3:
            print('Телефонная книга: \n')
            out.look_phone_book()
        elif command == 4:
            x = input_data.search_contact()
            print('Данные по вашему запросу: \n')
            out.search_view_number(x)
        elif command == 5:
            print('Работа завершена')
            break
        else:
            print('Ошибка')
