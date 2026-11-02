"""Command-line menu for the mining equipment store."""

from csv_storage import initialize_files
from inventory import list_products
from sales import calculate_total, create_sale, list_sales


def show_products():
    print("\n--- Товары в магазине ---")
    for product in list_products():
        print(
            f"{product['product_id']}. {product['name']} — "
            f"{product['price']} руб. | На складе: {product['quantity']} шт."
        )


def handle_sale():
    show_products()
    try:
        product_id = int(input("Номер товара: "))
        quantity = int(input("Количество: "))
        sale, remaining_stock = create_sale(product_id, quantity)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    print(f"Продано: {sale['product_name']} — {sale['quantity']} шт.")
    print(f"Сумма продажи: {sale['total']} руб.")
    print(f"Осталось на складе: {remaining_stock} шт.")


def show_sales():
    print("\n--- История продаж ---")
    sales = list_sales()
    if not sales:
        print("Продаж пока нет.")
        return
    for sale in sales:
        print(
            f"#{sale['sale_id']} | {sale['product_name']} | "
            f"{sale['quantity']} шт. | {sale['total']} руб."
        )


def run():
    initialize_files()
    while True:
        print("\n=== Учёт продаж ===")
        print("1 — Показать товары")
        print("2 — Продать товар")
        print("3 — Общая сумма продаж")
        print("4 — История продаж")
        print("0 — Выход")

        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_products()
        elif choice == "2":
            handle_sale()
        elif choice == "3":
            print(f"Общая сумма продаж: {calculate_total()} руб.")
        elif choice == "4":
            show_sales()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Ошибка: выберите пункт меню.")


if __name__ == "__main__":
    run()
