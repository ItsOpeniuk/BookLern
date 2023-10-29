import script
import rectangle
# Константы для элементов меню

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETR_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():

    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Выбери вариант : '))

        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга : '))
            print(f'Площадь равна круга -  {script.area(radius)}')
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга : '))
            print(f'Длинна окружности равна -  {script.circlurmfence(radius)}')
        elif choice == AREA_CIRCLE_CHOICE:
            width = float(input('Введите ширину прямоугольника : '))
            length = float(input('Введите длинну прямоугольника : '))
            print(f'Площадь прямоугольника равна -  {rectangle.area(width, length)}')
        elif choice == PERIMETR_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника : '))
            length = float(input('Введите длинну прямоугольника : '))
            print(f'Периметр прямоугольника равен - {rectangle.perimetr(width, length)}')
        elif choice == QUIT_CHOICE:
            print('Программа завершена!')
        else:
            print('Не корректный ввод ')


def display_menu():
    print('ЭТО МЕНЮ НАШЕЙ ПРОГРАММЫ')
    print('1. Площад круга. ')
    print('2. Длинна окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямоугольника')
    print('5. Выход с программы')


if __name__ == '__main__':
    main()