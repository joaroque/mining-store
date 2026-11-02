"""Sales operations: register purchases and calculate revenue."""

from datetime import datetime

import csv_storage as storage
from inventory import get_product, update_stock


def list_sales():
    """Return all sales saved in sales.csv."""
    return storage.read_rows(storage.SALES_FILE)


def create_sale(product_id, quantity):
    """Sell a product and save the sale and updated stock to CSV."""
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля.")

    product = get_product(product_id)
    if product is None:
        raise ValueError("Товар не найден.")
    if quantity > product["quantity"]:
        raise ValueError("Недостаточно товаров на складе.")

    current_sales = list_sales()
    next_sale_id = max((int(sale["sale_id"]) for sale in current_sales), default=0) + 1
    remaining_stock = product["quantity"] - quantity
    sale = {
        "sale_id": next_sale_id,
        "date": datetime.now().astimezone().isoformat(timespec="seconds"),
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total": product["price"] * quantity,
    }

    # If saving the sales log fails, restore the original stock.
    update_stock(product_id, remaining_stock)
    try:
        storage.write_rows(storage.SALES_FILE, storage.SALE_FIELDS, current_sales + [sale])
    except OSError:
        update_stock(product_id, product["quantity"])
        raise

    return sale, remaining_stock


def calculate_total():
    """Calculate total revenue from sales.csv, including previous runs."""
    return sum(int(sale["total"]) for sale in list_sales())
