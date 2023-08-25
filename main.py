import json
import os
import time

n_data = {
        'users':[]
    }
class User():
    def __init__(self):
        self.user_n = input('Введите имя:')
        self.user_f = input('Введите фамилию:')
        self.user_o = input('Введите отчество:')
        self.user_org = input('Название организации:')
        self.user_work_tel = input('Введите рабочий телефон:')
        self.user_tel = input('Введите личный телефон:')

# Custom function
def user_field_changes(user, data, field):
    """Функция принимает
        1 Пользователя
        2 Данные json
        3 Поле для изменения"""

    # Вводим новые данные
    user[field] = input('\nВведите изменение:')
    # Перезаписываем старое
    data["users"][0] = user

    return data

def back_menu():
    back = input("\nНажмите 0 для возврата в главное меню: ")
    if back != '0':
        back_menu()
    else:
        os.system("cls")
        allmenu()

def write(data, filename):
    """Запись в файл json"""

    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent =4)

def read(filename):
    """Чтение файла json"""

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Main menu //////////////////////////////////////////////////////
def menu1():
    """Выводим список абонентов"""

    data = read('data.json')

    print('Список абонентов\n')

    for i in range(0, len(data['users'])):
        print(data["users"][i]["user_n"], data["users"][i]["user_f"], data["users"][i]["user_o"], data["users"][i]["user_org"], data["users"][i]["user_work_tel"], data["users"][i]["user_tel"],'\n', sep=' ')

    back_menu()
def menu2():
    print("Поиск абонента...\n")

    data = read('data.json')

    user_n = str(input("Введите имя или фамилию абонента: "))
    user = [i for i in data["users"] if i['user_n'] == user_n or i['user_f'] == user_n]


    if not user:
        os.system("cls")
        print("Поиск абонента...\n\n Абонент не найден!!!!")
    else:
        os.system("cls")
        print(f"Поиск абонента...\n\n Найденые абоненты: {len(user)}\n")
        for i in user:
            print(i["user_n"], i["user_f"], i["user_o"], i["user_org"], i["user_work_tel"], i["user_tel"], sep=' ')

    back_menu()

def menu3():
    """Добавление абонента в абонентскую книжку"""

    print("Добавление абонента...\n")

    user = User().__dict__

    n_data['users'].append(user)

    print('\nДобавлен новый абонент: ',user["user_n"], user["user_f"], user["user_o"], user["user_org"], user["user_work_tel"], user["user_tel"], sep=' ')

    write(n_data, 'data.json')

    back_menu()

def menu4():
    """Редактирование абонента в абонентскую книжку"""

    data = read('data.json')
    print("Редактирование абонента.....\n")
    # Ищем абонента
    user_n = str(input("Введите имя или фамилию абонента: "))
    user = [i for i in data["users"] if i['user_n'] == user_n or i['user_f'] == user_n]

    if not user:
        os.system("cls")
        print("Поиск абонента...\n\n Абонент не найден!!!!\n")
        menu4()
    elif len(user) > 1:
        os.system("cls")
        print(f"Найденые абоненты: {len(user)}")
        for i in user:
            print('\n', i["user_n"], i["user_f"], i["user_o"], i["user_org"], i["user_work_tel"], i["user_tel"],'\n', sep=' ')
        print('Выберите одного из абонентов \n')
        menu4()
    # Забираем его данные
    user = data["users"][user.index(user[0])]

    # Выбор поля для изменения
    print('\nИзменить поле\n'
          '\n1. Имя\n'
          '2. Фамилию\n'
          '3. Отчество\n'
          '4. Организацию\n'
          '5. Рабочий телефон\n'
          '6. Сотовый телефон')

    # Меняем в зависимости от выбранного поля
    check = input("\nВыберите поле:")
    match check:
        case '1': user_field_changes(user, data, "user_n")
        case '2': user_field_changes(user, data, "user_f")
        case '3': user_field_changes(user, data, "user_o")
        case '4': user_field_changes(user, data, "user_org")
        case '5': user_field_changes(user, data, "user_work_tel")
        case '6': user_field_changes(user, data, "user_tel")

    # Перезаписываем
    write(data, 'data.json')



    print("\nИзменения внесены")

    time.sleep(0.6)

    os.system("cls")

    allmenu()
def allmenu():
    print('Справочник\n'
          '\n1. Список абонентов\n'
          '2. Поиск  абонента\n'
          '3. Добавить абонента\n'
          '4. Редактировать данные абонента\n')

    check = input("\nВыберите меню: ")

    os.system("cls")

    match check:
        case '1': menu1()
        case '2': menu2()
        case '3': menu3()
        case '4': menu4()

allmenu()