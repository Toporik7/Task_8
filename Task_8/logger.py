from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def copy_line():
    line_number = int(input('Введите номер строки: '))
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if line_number < 1 or line_number > len(lines):
        print('Некорректный номер строки')
        return
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        file.write(lines[line_number - 1])

        for i in range(len(lines)):
            if i != line_number - 1:
                file.write(lines[i])
    print('Копирование строки успешно выполнено')