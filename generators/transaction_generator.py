import random
import pandas as pd

from config.settings import OUTPUT_FOLDER, RANDOM_SEED


print(type(OUTPUT_FOLDER))
print(OUTPUT_FOLDER)

random.seed(RANDOM_SEED)


def generate_transactions():

    # ==========================
    # Load Dimension Tables
    # ==========================

    customer_df = pd.read_csv(f"{OUTPUT_FOLDER}/dim_customer.csv")
    product_df = pd.read_csv(f"{OUTPUT_FOLDER}/dim_product.csv")

    # Ambil hanya produk membership
    membership_products = product_df[
        product_df["category"] == "Membership"
    ]

    transactions = []

    # ==========================
    # Generate Membership Transaction
    # ==========================

    for _, customer in customer_df.iterrows():

        membership_name = customer['membership_preference'] +" Membership"

        membership = membership_products[
            membership_products["product_name"] == membership_name
        ]

        if membership.empty:
            print(
                f"Membership '{membership_name}' tidak ditemukan"
                f"untuk{customer['customer_id']}"
            )
            continue
        membership = membership.iloc[0]

        transaction = {
            "transaction_date": customer["join_date"],
            "customer_id": customer["customer_id"],
            "product_id": membership["product_id"],
            "quantity": 1,
            "unit_price": membership["price"],
            "discount_pct": 0,
            "discount_amount": 0,
            "total_amount": membership["price"],
            "payment_method": customer["preferred_payment"]
        }

        transactions.append(transaction)

    # ==========================
    # Convert to DataFrame
    # ==========================

    df = pd.DataFrame(transactions)

    # ==========================
    # Generate Transaction ID
    # ==========================

    df.insert(
        0,
        "transaction_id",
        [f"TRX{i:06d}" for i in range(1, len(df) + 1)]
    )

    # ==========================
    # Save CSV
    # ==========================

    df.to_csv(
        f"{OUTPUT_FOLDER}/fact_transaction.csv",
        index=False
    )

    print("Fact Transaction generated successfully!")