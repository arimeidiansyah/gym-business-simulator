import pandas as pd

from config.settings import OUTPUT_FOLDER

def load_customer_dimension():
    return pd.read_csv(f":{OUTPUT_FOLDER}/dim_customer.csv")

def load_product_dimension():
    return pd.read_csv(f":{OUTPUT_FOLDER}/dim_product.csv")

def load_membership_dimension():
    return pd.read_csv(f":{OUTPUT_FOLDER}/dim_membership.csv")