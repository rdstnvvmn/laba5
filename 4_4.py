def family_tree_heights():
    try:
        N = int(input("Введите количество человек: "))
        if N <= 0:
            print("Ошибка. Количество человек должно быть положительным числом.")
            return

        relations = {}
        all_people = set()

        for i in range(N - 1):
            while True:
                try:
                    pair = input(f"{i + 1} пара: ").strip()
                    if not pair:
                        print("Ошибка. Ввод не может быть пустым. Попробуйте снова.")
                        continue

                    parts = pair.split()
                    if len(parts) != 2:
                        print("Ошибка. Введите ровно два имени, разделённых пробелом. Попробуйте снова.")
                        continue

                    descendant, parent = parts
                    if descendant == parent:
                        print("Ошибка. Потомок не может быть своим собственным родителем. Попробуйте снова.")
                        continue

                    relations[descendant] = parent
                    all_people.add(descendant)
                    all_people.add(parent)
                    break
                except Exception as e:
                    print(f"Ошибка ввода: {e}. Попробуйте снова.")

        if not all_people:
            print("Ошибка. Не указано ни одного человека.")
            return

        root = None
        descendants = set(relations.keys())
        potential_roots = all_people - descendants

        if len(potential_roots) != 1:
            print("Ошибка. В дереве должен быть ровно один корень (родоначальник).")
            return

        root = potential_roots.pop()
        heights = {}

        def find_height(person):
            if person in heights:
                return heights[person]
            if person == root:
                heights[person] = 0
            else:
                if person not in relations:
                    heights[person] = 0
                else:
                    heights[person] = find_height(relations[person]) + 1
            return heights[person]

        for person in all_people:
            find_height(person)

        print("\n“Высота” каждого члена семьи:")
        for person in sorted(all_people):
            print(person, heights[person])

    except ValueError:
        print("Ошибка. Введите целое число для количества человек.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    family_tree_heights()