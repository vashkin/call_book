from platform import java_ver
from re import search
import function_book

fbook = function_book
data = []


def start(data):
    print("список контактов:")
    for i in data:
        print("{} {}  номер телефона: {} {}".format(i[0], i[1], i[2], i[3]))
    print("***********          Помощь.        ************* \n*** Для поиска - введите команду 's'          *** \n*** Для экспорта файла  - введите команду 'e' *** \n*** Для импорта файла - введите команду 'i'   *** ")
    command = input()
    if command == "s":
        search = input("кого будем искать? ")
        print(fbook.search_contact(data, search))
    elif command == "e":
        exp = input("format export command 'j' for json 'c' for csv ")
        if exp == 'j':
            fbook.export_json(input("Введите имя файла "), data)
        elif exp == 'c':
            fbook.export_csv(input("Введите имя файла "), data)
    elif command == "i":
        imp = input("format import command 'j' for json 'c' for csv ")
        if imp == 'j':
            data = fbook.import_json(input("Введите имя файла "))
        elif imp == 'c':
            data = fbook.import_csv(input("Введите имя файла "))
    start(data)


start(data)
