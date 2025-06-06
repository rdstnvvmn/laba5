def countries_and_cities():
    while True:
        try:
            k = int(input("Введите количество стран: "))
            if k <= 0:
                print("Количество стран должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")

    countries = {}

    print("Введите данные для стран (Страна Город1 Город2 ...):")
    for i in range(k):
        while True:
            line_input = input(f"{i + 1} страна: ").strip()
            if not line_input:
                print("Ввод не может быть пустым.")
                continue
            line = line_input.split()
            if len(line) < 2:
                print(f"Некорректный ввод для страны {i + 1}. "
                      "Ожидается: Страна Город1 Город2 ...")
                continue
            country = line[0]
            cities = line[1:]
            valid_cities = [city for city in cities if city]
            if not valid_cities:
                print(f"Некорректный ввод для страны {i + 1}. "
                      "Города не указаны.")
                continue
            for city in valid_cities:
                countries[city] = country
            break

    if k > 0:
        print("\nВведите 3 города для поиска информации:")
        for i in range(3):
            while True:
                city_to_find = input(f"{i + 1} город: ").strip()
                if city_to_find:
                    break
                else:
                    print("Название города не может быть пустым.")

            if city_to_find in countries:
                print(f"Город {city_to_find} расположен в стране "
                      f"{countries[city_to_find]}.")
            else:
                print(f"По городу {city_to_find} данных нет.")


if __name__ == '__main__':
    countries_and_cities()