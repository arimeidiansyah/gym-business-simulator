import random
import pandas as pd

from config.settings import OUTPUT_FOLDER, RANDOM_SEED
from utils.journey import simulate_customer
from utils.event_id import assign_event_id


print(type(OUTPUT_FOLDER))
print(OUTPUT_FOLDER)

random.seed(RANDOM_SEED)


def generate_customer_events():

    # ==========================
    # Load Dimension Tables
    # ==========================

    customer_df = pd.read_csv(f"{OUTPUT_FOLDER}/dim_customer.csv")

    customer_df["join_date"] = pd.to_datetime(customer_df["join_date"])

    all_events = []

    for _, customer in customer_df.iterrows():

        customer_events = simulate_customer(customer)

        all_events.extend(customer_events)
    
    all_events = assign_event_id(all_events)

    first_customer = customer_df.iloc[0]["customer_id"]

    customer_events = [
        e for e in all_events
        if e["customer_id"] == first_customer
    ]

    for event in customer_events[:20]:
        print(event)

    return
