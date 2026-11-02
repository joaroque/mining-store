"""CSV file operations for the mining equipment shop."""

import csv
import os
import tempfile
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
PRODUCTS_FILE = DATA_DIR / "products.csv"
SALES_FILE = DATA_DIR / "sales.csv"

PRODUCT_FIELDS = ["product_id", "name", "price", "quantity"]
SALE_FIELDS = [
    "sale_id", "date", "product_id", "product_name",
    "quantity", "unit_price", "total",
]

INITIAL_PRODUCTS = [
    {"product_id": 1, "name": "Каска", "price": 1500, "quantity": 10},
    {"product_id": 2, "name": "Перчатки", "price": 500, "quantity": 20},
    {"product_id": 3, "name": "Фонарь", "price": 2000, "quantity": 5},
]


def read_rows(file_path):
    """Read a semicolon-separated CSV file as dictionaries."""
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def write_rows(file_path, field_names, rows):
    """Write a CSV safely, replacing the file after successful creation."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None

    try:
        with tempfile.NamedTemporaryFile(
            "w", dir=file_path.parent, encoding="utf-8-sig",
            newline="", delete=False, suffix=".tmp"
        ) as file:
            temporary_path = Path(file.name)
            writer = csv.DictWriter(file, fieldnames=field_names, delimiter=";")
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary_path, file_path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def initialize_files():
    """Create example products and an empty sales log if needed."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not PRODUCTS_FILE.exists():
        write_rows(PRODUCTS_FILE, PRODUCT_FIELDS, INITIAL_PRODUCTS)
    if not SALES_FILE.exists():
        write_rows(SALES_FILE, SALE_FIELDS, [])
