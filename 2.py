from collections import defaultdict


def get_number_of_orders():
    """Запрашивает у пользователя количество заказов.

    Returns:
        int: Количество заказов (неотрицательное целое число).
    """
    while True:
        try:
            n = int(input("Введите кол-во заказов: "))
            if n >= 0:
                return n
            else:
                print("Количество заказов не может быть отрицательным.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def input_pizza_orders(num_orders):
    """Собирает данные о заказах пиццы.

    Args:
        num_orders (int): Количество заказов для ввода.

    Returns:
        defaultdict: Словарь с данными о заказах, сгруппированными по покупателям.
    """
    orders = defaultdict(lambda: defaultdict(int))
    if num_orders == 0:
        print("Количество заказов равно 0, ввод данных пропускается.")
        return orders

    print("Введите заказы (формат: Покупатель НазваниеПиццы Количество):")
    for i in range(1, num_orders + 1):
        while True:
            order_str = input(f"{i} заказ: ").strip()
            if not order_str:
                print("Ввод не может быть пустым.")
                continue

            order_parts = order_str.split()
            if len(order_parts) != 3:
                print("Некорректный формат. Ожидается: "
                      "Покупатель НазваниеПиццы Количество (3 слова).")
                continue

            customer, pizza, quantity_str = order_parts
            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("Количество пицц должно быть положительным числом.")
                    continue
            except ValueError:
                print("Количество пицц должно быть целым числом.")
                continue

            orders[customer][pizza] += quantity
            break
    return orders


def print_customer_orders(orders_data):
    """Выводит информацию о заказах, отсортированную по покупателям и названиям пицц.

    Args:
        orders_data (defaultdict): Словарь с данными о заказах.
    """
    if not orders_data:
        print("\nНет заказов для отображения.")
        return

    print("\nДетализированные заказы по клиентам:")
    for customer in sorted(orders_data.keys()):
        print(f"{customer}:")
        sorted_pizzas = sorted(orders_data[customer].items())
        for pizza, quantity in sorted_pizzas:
            print(f"  {pizza}: {quantity}")
        print()


def main():
    """Основная функция для обработки заказов пиццы."""
    print("--- Обработка заказов пиццы ---")
    num_orders = get_number_of_orders()
    customer_orders = input_pizza_orders(num_orders)
    print_customer_orders(customer_orders)


if __name__ == "__main__":
    main()