def guess_the_number():
    while True:
        try:
            N = int(input("Введите максимальное число: "))
            if N < 1:
                print("Число должно быть положительным. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Ошибка. Введите целое положительное число.")

    hidden_num = [str(i) for i in range(1, N + 1)]  # Возможные числа от 1 до N

    while True:
        while True:
            print("Введите 'Помогите!', если не можете отгадать")
            input_Ser = input("Нужное число есть среди вот этих чисел: ").split()
            if input_Ser[0] == "Помогите!":
                print(f'Иван мог загадать следующие числа: {" ".join(hidden_num)}')
                return

            try:
                for num in input_Ser:
                    if not num.isdigit():
                        raise ValueError
                    if int(num) < 1 or int(num) > N:
                        print(f"Числа должны быть от 1 до {N}. Попробуйте снова.")
                        raise ValueError
                break
            except ValueError:
                print(f"Ошибка. Введите числа от 1 до {N} через пробел или 'Помогите!'.")
                continue

        while True:
            input_Iv = input("Ответ Ивана: ")
            if input_Iv in ["Да", "Нет"]:
                break
            print("Ошибка: ответ должен быть 'Да' или 'Нет'.")

        if input_Iv == "Да":
            hidden_num = [num for num in input_Ser if num in hidden_num]
            if len(hidden_num) == 1:
                print(f'Иван загадал число: {" ".join(hidden_num)}')
                return

        if input_Iv == "Нет":
            new_hidden_num = [num for num in hidden_num if num not in input_Ser]
            if not new_hidden_num:
                print("Ошибка. Иван не мог загадать такое число, так как других вариантов нет!")
                return
            hidden_num = new_hidden_num

if __name__ == "__main__":
    guess_the_number()