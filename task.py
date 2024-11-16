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