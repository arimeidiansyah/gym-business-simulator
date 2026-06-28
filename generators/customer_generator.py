import random
from pathlib import Path
from datetime import timedelta

import numpy as np
import pandas as pd
from faker import Faker

import config

fake = Faker("id_ID")

# ---------------------------------------------------
# Setting
# ---------------------------------------------------

random.seed(config.RANDOM_SEED)
np.random.seed(config.RANDOM_SEED)


# ---------------------------------------------------
# Helper Functions
# ---------------------------------------------------

def generate_customer_id(number):
    return f"CUST{number:05d}"


def random_birth_date():

    age_group = random.choices(
        population=[
            (18, 24),
            (25, 34),
            (35, 44),
            (45, 55),
            (56, 65)
        ],
        weights=[25, 45, 20, 8, 2],
        k=1
    )[0]

    age = random.randint(age_group[0], age_group[1])

    today = config.END_DATE

    birth = today - timedelta(days=age * 365 + random.randint(0, 364))

    return birth.date(), age


def random_join_date():

    total_days = (config.END_DATE - config.START_DATE).days

    return (
        config.START_DATE +
        timedelta(days=random.randint(0, total_days))
    ).date()

# ---------------------------------------------------
# Main Generator
# ---------------------------------------------------

def generate_customers():

    project_root = Path(__file__).resolve().parent.parent

    persona_df = pd.read_csv(
        project_root / "data" / "persona_master.csv"
    )

    payment_df = pd.read_csv(
        project_root / "data" / "payment_method_master.csv"
    )

    cities = [
        "Bekasi",
        "Jakarta",
        "Depok",
        "Bogor",
        "Tangerang"
    ]

    city_weights = [45, 25, 10, 10, 10]

    rows = []

    for i in range(1, config.TOTAL_CUSTOMERS + 1):

        gender = random.choices(
            ["Male", "Female"],
            weights=[60, 40],
            k=1
        )[0]

        if gender == "Male":
            name = fake.name_male()
        else:
            name = fake.name_female()

        birth_date, age = random_birth_date()

        persona = random.choices(
            persona_df["persona_name"],
            weights=persona_df["percentage"],
            k=1
        )[0]

        payment = random.choice(
            payment_df["payment_method"]
        )

        city = random.choices(
            cities,
            weights=city_weights,
            k=1
        )[0]

        status = random.choices(
            ["Active", "Inactive"],
            weights=[90, 10],
            k=1
        )[0]

        rows.append({

            "customer_id": generate_customer_id(i),

            "customer_name": name,

            "gender": gender,

            "birth_date": birth_date,

            "age": age,

            "city": city,

            "join_date": random_join_date(),

            "persona": persona,

            "preferred_payment": payment,

            "status": status

        })

    df = pd.DataFrame(rows)

    output = project_root / "output" / "dim_customer.xlsx"

    df.to_excel(output, index=False)

    print(f"✅ Customer Dimension : {len(df)} rows")