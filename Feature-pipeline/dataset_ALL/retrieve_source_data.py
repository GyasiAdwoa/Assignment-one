import os
import pandas as pd
from tqdm import tqdm
from enum import Enum

class Dataset(Enum):
    CUSTOMERS = "olist_customers_dataset.csv"
    GEOLOCATION = "olist_geolocation_dataset.csv"
    ORDER_ITEMS = "olist_order_items_dataset.csv"
    ORDER_PAYMENTS = "olist_order_payments_dataset.csv"
    ORDER_REVIEWS = "olist_order_reviews_dataset.csv"
    ORDERS = "olist_orders_dataset.csv"
    PRODUCTS = "olist_products_dataset.csv"
    SELLERS = "olist_sellers_dataset.csv"

    def __str__(self):
        return str(self.value)

def fetch_data(dataset: Dataset, output_filename: str):
    print(f"Reading dataset: {dataset.value}")
    file_path = os.path.join("C:\Users\HP USER\Downloads\Assignment-one-1\Feature-pipeline\dataset_ALL", dataset.value)  # Update the path to your dataset directory
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    
    with tqdm(total=os.path.getsize(file_path), unit="iB", unit_scale=True, unit_divisor=1024, desc=dataset.value) as progress_bar:
        df = pd.read_csv(file_path)
        df.to_csv(output_filename, index=False)
        progress_bar.update(os.path.getsize(file_path))

    print("Done")

if __name__ == "__main__":
    fetch_data(Dataset.CUSTOMERS, "olist_customers_dataset.csv")
    fetch_data(Dataset.GEOLOCATION, "geolocation.csv")
    fetch_data(Dataset.ORDER_ITEMS, "order_items.csv")
    fetch_data(Dataset.ORDER_PAYMENTS, "order_payments.csv")
    fetch_data(Dataset.ORDER_REVIEWS, "order_reviews.csv")
    fetch_data(Dataset.ORDERS, "orders.csv")
    fetch_data(Dataset.PRODUCTS, "products.csv")
    fetch_data(Dataset.SELLERS, "sellers.csv")
