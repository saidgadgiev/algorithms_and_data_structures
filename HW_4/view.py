
def greetings():
    print("\nДобро пожаловать в программу!\n")
    print("*ТЕЛЕФОННАЯ КНИГА*\n")
    
def menu():
    print("---МЕНЮ---\n")
    print("1. Добавление нового пользователя")
    print("2. Считыание данных из телефонной книги")
    print("3. Поиск")
    print("4. Изменение данных")
    print("5. Удаление данных")
    print("6. Выход\n")
    command = int(input('Выберите пункт МЕНЮ: '))
    return command

def show_contact_form():
    family = input('Введите фамилию: ').capitalize()
    name = input('Введите имя: ').capitalize()
    phone = input('Введите номер телефона: ')
    contact = {'family': family, 'name': name, 'phone': phone}
    return contact

def show_phonebook(book):
    for i in book:
        print(i)

def show_message(message):
    print(message)

def get_search_query():
    search_name = input("Введите полностью или часть фамилии, имени или телефона: ").capitalize()
    return search_name