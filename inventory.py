"""Inventory operations: load products, find products and update stock."""

import csv_storage as storage


def list_products():
    """Return products with numeric identifiers, prices and quantities."""
    products = storage.read_rows(storage.PRODUCTS_FILE)
    for product in products:
        product["product_id"] = int(product["product_id"])
        product["price"] = int(product["price"])
        product["quantity"] = int(product["quantity"])
    return products


def get_product(product_id):
    """Return one product, or None if it does not exist."""
    for product in list_products():
        if product["product_id"] == product_id:
            return product
    return None


def update_stock(product_id, new_quantity):
    """Save a product's new stock quantity in the products CSV."""
    if new_quantity < 0:
        raise ValueError("Stock cannot be negative")

    products = list_products()
    for product in products:
        if product["product_id"] == product_id:
            product["quantity"] = new_quantity
            storage.write_rows(storage.PRODUCTS_FILE, storage.PRODUCT_FIELDS, products)
            return
    raise ValueError("Product not found")
