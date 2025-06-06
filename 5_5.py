def vocabulary_test():
    try:
        try:
            with open("rus.txt", "r", encoding='utf-8') as file_rus, \
                    open("eng.txt", "r", encoding='utf-8') as file_eng:

                words_rus = [line.strip() for line in file_rus if line.strip()]
                words_eng = [line.strip() for line in file_eng if line.strip()]

                if len(words_rus) != len(words_eng):
                    print("Ошибка. Количество строк в файлах не совпадает!")
                    return

                if not words_rus or not words_eng:
                    print("Ошибка. Один или оба файла пустые!")
                    return

                good_ans = 0
                total_words = len(words_rus)

                if total_words < 3:
                    print("Ошибка. Слишком мало слов для тестирования (<3).")
                    return

                for i, (rus_word, eng_word) in enumerate(zip(words_rus, words_eng), 1):
                    print(f"Слово {i} из {total_words}: {rus_word}")
                    user_word = input("Введите перевод слова: ").strip()

                    if not user_word:
                        print("Вы не ввели ответ! Считается как ошибка.\n")
                        continue

                    if user_word.lower() == eng_word.lower():
                        print("Верно!\n")
                        good_ans += 1
                    else:
                        print(f"Неверно. Правильный ответ: {eng_word}\n")

                mark = good_ans / total_words
                print(f"\nРезультат: {good_ans} из {total_words} правильных ответов")

                if mark >= 0.85:
                    print('Ваша оценка: 5 (Отлично)')
                elif 0.65 <= mark < 0.85:
                    print('Ваша оценка: 4 (Хорошо)')
                elif 0.45 <= mark < 0.65:
                    print('Ваша оценка: 3 (Удовлетворительно)')
                else:
                    print('Ваша оценка: 2 (Неудовлетворительно)')

        except FileNotFoundError as e:
            print(f"Ошибка: файл не найден - {e.filename}")
        except IOError as e:
            print(f"Ошибка ввода-вывода: {e}")
        except UnicodeDecodeError:
            print("Ошибка: проблемы с кодировкой файла (должна быть UTF-8)")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    vocabulary_test()