import pandas as pd

from config.settings import OUTPUT_FOLDER

TRANSACTION_EVENTS = [
    "Membership",
    "Supplement",
    "Merchandise",
    "Personal Training"
]

def generate_fact_transaction():

    event_df = pd.read_csv(
        OUTPUT_FOLDER / "fact_event_log.csv",
        parse_dates=["event_date"]
    )

    product_df = pd.read_csv(
        OUTPUT_FOLDER / "dim_product.csv"
    )

    transaction_df = event_df[
        event_df["event_type"].isin(TRANSACTION_EVENTS)
    ].copy()

    print(transaction_df["product_id"].unique())

    transaction_df = transaction_df.merge(
        product_df[["product_id","price"]],
        on="product_id",
        how="left"
    )

    transaction_df.rename(
        columns={
            "event_date": "transaction_date",
            "price": "unit_price"
        },
        inplace=True
    )

    transaction_df = transaction_df[
    [
        "transaction_date",
        "customer_id",
        "product_id",
        "unit_price",
        "payment_method"
    ]
]

    transaction_df.insert(
        0,
        "transaction_id",
        [
            f"TRX{i:06d}"
            for i in range(
                1, len(transaction_df) + 1)
        ]
    )


    transaction_df.to_csv(
        OUTPUT_FOLDER / "fact_transaction.csv",
        index=False
    )

    print("✅ Fact Transaction : {} rows".format(len(transaction_df)))

    print(transaction_df["transaction_id"].duplicated().sum())
    print(transaction_df["customer_id"].isna().sum())
    print(transaction_df["product_id"].isna().sum())
    print(transaction_df["unit_price"].isna().sum())