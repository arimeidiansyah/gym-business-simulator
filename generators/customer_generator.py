import random
from pathlib import Path
from datetime import timedelta

import numpy as np
import pandas as pd
from faker import Faker
from utils.name_utils import clean_name

from config.settings import (
    TOTAL_CUSTOMERS,
    START_DATE,
    END_DATE,
    RANDOM_SEED
)

from config.business_rules import (
    GENDER_DISTRIBUTION,
    CITY_DISTRIBUTION,
    AGE_DISTRIBUTION
)

from config.persona_rules import (
    PERSONA_PROFILE,
    PERSONA_DISTRIBUTION
)

from config.payment_rules import PAYMENT_BEHAVIOUR

fake = Faker("id_ID")

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


# =========================================================
# Helper Functions
# =========================================================

def generate_customer_id(number):
    return f"CUST{number:05d}"


def random_birth_date():

    age_group = random.choices(
        population=list(AGE_DISTRIBUTION.keys()),
        weights=list(AGE_DISTRIBUTION.values()),
        k=1
    )[0]

    age = random.randint(age_group[0], age_group[1])

    birth = END_DATE - timedelta(
        days=age * 365 + random.randint(0, 364)
    )

    return birth.date(), age


def random_join_date():

    total_days = (END_DATE - START_DATE).days

    return (
        START_DATE +
        timedelta(days=random.randint(0, total_days))
    ).date()


def choose_persona():

    return random.choices(
        population=list(PERSONA_DISTRIBUTION.keys()),
        weights=list(PERSONA_DISTRIBUTION.values()),
        k=1
    )[0]


def choose_payment(persona):

    payment_rule = PAYMENT_BEHAVIOUR[persona]

    return random.choices(
        population=list(payment_rule.keys()),
        weights=list(payment_rule.values()),
        k=1
    )[0]


# =========================================================
# Main Generator
# =========================================================

def generate_customers():

    project_root = Path(__file__).resolve().parent.parent

    rows = []

    for i in range(1, TOTAL_CUSTOMERS + 1):

        gender = random.choices(
            population=list(GENDER_DISTRIBUTION.keys()),
            weights=list(GENDER_DISTRIBUTION.values()),
            k=1
        )[0]

        if gender == "Male":
            name = clean_name(fake.name_male())
        else:
            name = clean_name(fake.name_female())

        birth_date, age = random_birth_date()

        city = random.choices(
            population=list(CITY_DISTRIBUTION.keys()),
            weights=list(CITY_DISTRIBUTION.values()),
            k=1
        )[0]

        persona = choose_persona()

        payment = choose_payment(persona)

        membership_preference = random.choice(
            PERSONA_PROFILE[persona]["membership_preference"]
        )

        membership_product_map = {
            "Monthly" : "MEM001",
            "Quarterly":"MEM002",
            "Semi Annual":"MEM003",
            "Annual":"MEM004"
        }

        membership_product_id = membership_product_map[membership_preference]

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

            "membership_preference": membership_preference,

            "membership_product_id": membership_product_id,

            "status": status

        })

    df = pd.DataFrame(rows)

    output = project_root / "output" / "dim_customer.csv"

    df.to_csv(output, index=False)

    print(f"✅ Customer Dimension : {len(df)} rows")


if __name__ == "__main__":
    generate_customers()