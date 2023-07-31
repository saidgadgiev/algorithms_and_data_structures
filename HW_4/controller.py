import model
import view


def run():
    view.greetings()

    while True:

        command = view.menu()

        if command == 1:
            data = view.show_contact_form()
            model.add_contact(data)

            view.show_message('Контакт успешно добавлен')

        if command == 2:
            data = model.read_phonebook()
            view.show_phonebook(data)

        if command == 3:
            search = view.get_search_query()
            data = model.find(search)
            if len(data) == 0:
                view.show_message('Пользователь не найден')
            else:
                view.show_phonebook(data)

        if command == 4:
            view.show_message('Введите поисковую фразу')
            search = view.get_search_query()
            data = model.find_first(search)
            if len(data) == 0:
                view.show_message('Пользователь не найден')
            else:
                view.show_phonebook(data)
                view.show_message('Введите новые данные пользователя')
                data = view.show_contact_form()
                model.find_and_change(search, data)
                view.show_message('Данные успешно изменены')

        # Удаление данных:
        # во view изспользуем функцию из предыдущего пункта get_search_query, возвращается строка с поисковой фразой
        # model производит поиск подстроки, и удаляет первого подходящего пользователя, возвращает True, если пользователь найден, False - если не найден
        if command == 5:
            view.show_message('Введите поисковую фразу')
            search = view.get_search_query()
            found = model.find_and_del_first(search)
            if found == False:
                view.show_message('Пользователь не найден')
            else:
                view.show_message('Пользователь успешно удалён')

        if command == 6:
            break
