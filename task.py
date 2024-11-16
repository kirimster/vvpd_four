def display_menu():
    """Меню"""
    print(
        "\nДобро пожаловать в меню,что вы хотите сделать?:\n"
        "1. Ввести размер массива\n"
        "2. Создать массив\n"
        "3. Просмотр массива\n"
        "4. Выполнение функций\n"
        "5. Выход\n"
    )


def display_func_menu():
    """Показ функций для работы с матрицами"""
    print("\nКакую функцию хотите выполнить?:\n"
        "1. Замена всех элементов, которые меньше 10, числом 42\n"
        "2. Печть индексов отрицательных элементов массива\n"
        "3. Вычисление суммы элементов каждого столбца и строки\n"
        "4. Вывести левую и правую диагональ двумерного массива\n"
        "5. Нахождение столбца с наибольшой суммой элементов\n"
        "6. Выход в меню\n")

def display_create_massive():
    print("\nКак вы хотите заполнить массив?:\n"
          "1. Ввести значения вручную\n"
          "2. Заполнить числами наугад\n"
          "3. Выход в меню\n"
          )


def size_matrix():
    """Ввод размера массива"""
    print("\nВвод размера матрицы\n")
    try:
        m=int(input("Сколько будет строчек?: "))
        if m<0:
            raise ValueError("Число должно быть положительным!!!")
        n=int(input("\nСколько будет столбцов?: "))
        if n<0:
            raise ValueError("Число должно быть положительным!!!")
    except ValueError as err:
        print(err.args)
        print("Ошибка: Неверный ввод. Пожалуйста, введите корректные данные.")


def create_massive():
    """Создание массива"""
    while True:
        display_create_massive()
        menu_create_variable = input("Выберите опцию: ")
        match menu_create_variable:
            case "3":
                break



def replace_numbers():
    """Замена чисел на 42"""
    return 1

def main():
    """Основная функция"""
    while True:
        display_menu()
        menu_variable = input("Выберите опцию: ")
        match menu_variable:
            case "1":
                size_matrix()
            case "2":
                create_massive()
            case "4":
                while True:
                    display_func_menu()
                    menu_func_variable = input("Выберите опцию: ")
                    match menu_func_variable:
                        case "1":
                            replace_numbers()
                        case "6":
                            break
                        case _:
                            print("Ошибка: Неверный выбор. Пожалуйста, попробуйте снова.")
            case "5":
                break
            case _:
                print("Ошибка: Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
