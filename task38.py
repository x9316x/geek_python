import os
import re

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, "phonebook.txt")

def show_all_records():
    try:
        with open(file_path, 'r', encoding="utf-8") as data:
            for line in data:
                phonebook_data = line.replace(";", " ")
                print(phonebook_data, end="")
    except FileNotFoundError:
        print("Телефонный справочник пуст или файл не найден.")

def search_record():
    search = input("Введите данные для поиска (Фамилия, Имя или Отчество): ").lower()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if search in line.lower():
                    print(line.replace(";", " "), end="")
    except FileNotFoundError:
        print("Телефонный справочник пуст или файл не найден.")

def validate_phone_number(phone_number):
    if re.match(r'\+?\d{10,15}$', phone_number):
        return True
    return False

def add_contact(new_contact_fio, new_contact_number):
    if validate_phone_number(new_contact_number):
        with open(file_path, "a", encoding="utf-8") as f:
            if os.stat(file_path).st_size != 0:
                f.write("\n")
            f.write(new_contact_fio.replace(" ", ";"))
            f.write(';')
            f.write(new_contact_number)
    else:
        print("Введен некорректный номер телефона.")

def modify_contact():
    search = input("Введите данные для поиска (Фамилия, Имя или Отчество): ").lower()
    found = False
    records = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                record = line.strip()
                if search in record.lower():
                    found = True
                    print("Найденная запись:", record.replace(";", " "))
                    print("Введите новые данные.")
                    fio = input("Введите ФИО через пробел: ")
                    number = input("Введите Номер: ")
                    if validate_phone_number(number):
                        records.append(f"{fio.replace(' ', ';')};{number}")
                    else:
                        print("Введен некорректный номер телефона. Запись не изменена.")
                        records.append(record)
                else:
                    records.append(record)
        if found:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(records))
        else:
            print("Запись не найдена.")
    except FileNotFoundError:
        print("Телефонный справочник пуст или файл не найден.")

def delete_contact():
    search = input("Введите данные для поиска (Фамилия, Имя или Отчество): ").lower()
    found = False
    records = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                record = line.strip()
                if search in record.lower():
                    found = True
                    print("Найденная запись:", record.replace(";", " "))
                    print("Запись удалена.")
                else:
                    records.append(record)
        if found:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(records))
        else:
            print("Запись не найдена.")
    except FileNotFoundError:
        print("Телефонный справочник пуст или файл не найден.")


def main():
    while True:
        print("\nВыберите действие: 1 - Показать справочник,"
              "2 - найти контакт,"
              "3 - добавить контакт,"
              "4 - изменить контакт,"
              "5 - удалить контакт,"
              "0 - выход")
        try:
            select = int(input())
            if select == 1:
                show_all_records()
            elif select == 2:
                search_record()
            elif select == 3:
                fio = input("Введите ФИО через пробел: ")
                number = input("Введите Номер: ")
                add_contact(fio, number)
            elif select == 4:
                modify_contact()
            elif select == 5:
                delete_contact()
            elif select == 0:
                break
            else:
                print("Неизвестное действие, попробуйте еще раз.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
