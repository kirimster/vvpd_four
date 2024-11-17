import random
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
        "2. Печать индексов отрицательных элементов массива\n"
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
        n=int(input("Сколько будет столбцов?: "))
        if n<0:
            raise ValueError("Число должно быть положительным!!!")
    except ValueError as err:
        print(err.args)
        print("Ошибка: Неверный ввод. Пожалуйста, введите корректные данные.")
    print(f"Ваш массив будет размерностью: {m} X {n}")
    return m, n

def create_massive_hand(m, n):
    array = []
    for i in range(m):
        row = []
        for j in range(n):
            value = int(input(f"Введите элемент для массива [{i+1}][{j+1}]: "))
            row.append(value)
        array.append(row)
    return array


def create_massive_random(m, n):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]


def create_massive(m, n):
    """Создание массива"""
    try:
        if not(n>0 and m>0):
            raise ValueError("У вас не задана размерность матрицы!")

        while True:
            display_create_massive()
            menu_create_variable = input("Выберите опцию: ")
            match menu_create_variable:
                case "1":
                    array = create_massive_hand(m, n)
                case "2":
                    array = create_massive_random(m, n)
                case "3":
                    break
            return array
    except ValueError as err:
        print(err.args)


def print_matrix(array, m, n):
    try:
        if not array or not array[0]:
            raise ValueError("У вас нет матрицы для просмотра!")
        for row in array:
            print(" ".join(map(str,row)))
    except ValueError as err:
        print(err.args)

def replace_numbers(array, m, n):
    try:
        if not array or not array[0]:
            raise ValueError("У вас нет матрицы для выполнения этого действия!")
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] < 10:
                    array[i][j] = 42
        print_matrix(array)
        return array
    except ValueError as err:
        print(err.args)


def negative_numbers(array, m, n):
    try:
        if not array or not array[0]:
            raise ValueError("У вас нет матрицы для выполнения этого действия!")
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] < 0:
                    print(f"Индекс отрицательного элемента: [{i}][{j}]")
    except ValueError as err:
        print(err.args)


def sum_m_and_n(array, m, n):
    try:
        if not array or not array[0]:
            raise ValueError("У вас нет матрицы для выполнения этого действия!")
        sum_m = [sum(m) for m in array]
        sum_n = [sum(array[i][j] for i in range(len(array))) for j in range(len(array[0]))]
        print(f"Сумма строк равна: {sum_m}")
        print(f"Сумма столбцов равна: {sum_n}")
    except ValueError as err:
        print(err.args)



def diagonal_matrix(array, m, n):
    try:
        if not array or not array[0]:
            raise ValueError("У вас нет матрицы для выполнения этого действия!")
        if len(array) == len(array[0]):
            left = []
            right = []
            for i in range(len(array)):
                left.append(array[i][i])
                right.append(array[i][len(array)-1-i])
            print(f"Левая диагональ: {left}")
            print(f"Правая диагональ: {right}")
        else:
            print("У вас не квадратная матрица, не получится вывести правую и левую диагональ")
    except ValueError as err:
        print(err.args)



def max_n(array, m, n):
    try:
        if not array or not array[0]:
            raise ValueError("У вас нет матрицы для выполнения этого действия!")

        n_sums = [0] * n

        for i in range(n):
            for j in range(m):
                n_sums[j] += array[i][j]

        max_sum_index = 0
        max_sum_value = n_sums[0]

        for j in range(1, n):
            if n_sums[j] > max_sum_value:
                max_sum_value = n_sums[j]
                max_sum_index = j

        print(f"Самая большая сумма находится в столбце под номером {max_sum_index+1}")
    except ValueError as err:
        print(err.args)


def main():
    """Основная функция"""
    m, n = 0, 0
    array = []
    while True:
        display_menu()
        menu_variable = input("Выберите опцию: ")
        match menu_variable:
            case "1":
                m, n = size_matrix()
            case "2":
                array = create_massive(m, n)
            case "3":
                print_matrix(array, m, n)
            case "4":
                while True:
                    display_func_menu()
                    menu_func_variable = input("Выберите опцию: ")
                    match menu_func_variable:
                        case "1":
                            replace_numbers(array, m, n)
                        case "2":
                            negative_numbers(array, m, n)
                        case "3":
                            sum_m_and_n(array, m, n)
                        case "4":
                            diagonal_matrix(array, m, n)
                        case "5":
                            max_n(array, m, n)
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