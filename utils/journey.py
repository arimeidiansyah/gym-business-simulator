import random
from datetime import datetime,timedelta

from config.renewal_rules import (RENEWAL_PROBABILITY, RENEWAL_DELAY)
from utils.event import create_event
from config.customer_behaviour import CUSTOMER_BEHAVIOUR
from config.settings import END_DATE

from pandas.tseries.offsets import DateOffset


def get_membership_duration(customer):
    membership = customer ["membership_preference"]

    duration_map = {
        "Monthly": 1,
        "Quarterly": 3,
        "Semi Annual": 6,
        "Annual": 12
    }
    return duration_map[membership]


def generate_visit_timestamp(visit_date):

    period = random.choices(
        ["morning","afternoon","evening"],
        weights=[20, 30, 50],
        k=1
    )[0]

    if period =="morning":
        hour = random.randint(5,9)

    elif period =="afternoon":
        hour = random.randint(10,16)
    
    else:
        hour = random.randint(17,22)

    minute = random.randint(0,59)

    duration = random.randint(40, 120)

    check_in = datetime.combine(
        visit_date.date(),
        datetime.min.time()
        ).replace(
            hour=hour,
            minute=minute
        )
    
    check_out = check_in + timedelta(minutes=duration)

    return(
        check_in,
        check_out,
        duration
    )


def generate_purchase_event(
        customer,
        visit_date,
        product_df,
        category,
        probability,
        event_type
):
    if random.random() > probability:
        return []
    
    category_df = product_df[
        product_df["category"] == category
    ]

    selected_product = category_df.sample(1).iloc[0]

    event = create_event(
        event_date = visit_date,
        customer_id = customer["customer_id"],
        event_type = event_type,
        product_id = selected_product["product_id"],
        payment_method = customer["preferred_payment"]
    )

    return [event]


def generate_monthly_visits(customer, month_start, product_df):

    behaviour = CUSTOMER_BEHAVIOUR[customer["persona"]]

    min_visits, max_visits = behaviour["visit_per_month"]

    total_visits = random.randint(min_visits, max_visits)

    visit_days = sorted(
        random.sample(range(1, 29), total_visits)
    )

    events = []

    pt_purchased = False

    for day in visit_days:

        visit_date = month_start.replace(day=1) + timedelta(days=day - 1)

        if visit_date < customer["join_date"]:
            continue

        check_in, check_out, duration = generate_visit_timestamp(visit_date)

        events.append(
            create_event(
                event_date=visit_date,
                customer_id=customer["customer_id"],
                event_type="Visit",
                check_in=check_in,
                check_out=check_out,
                duration_minutes=duration
            )
        )

        supplement_events = generate_purchase_event(
            customer=customer,
            visit_date=visit_date,
            product_df=product_df,
            category="Supplement",
            probability=0.12,
            event_type="Supplement"
        )
        events.extend(supplement_events)

        merchandise_events = generate_purchase_event(
            customer=customer,
            visit_date=visit_date,
            product_df=product_df,
            category="Merchandise",
            probability=0.06,
            event_type="Merchandise"
        )

        events.extend(merchandise_events)

        if not pt_purchased:
            personal_training_events = generate_purchase_event(
                customer=customer,
                visit_date=visit_date,
                product_df=product_df,
                category="Personal Training",
                probability=0.02,
                event_type="Personal Training"
            )

            events.extend(personal_training_events)

            if len(personal_training_events) > 0:
                pt_purchased = True

    return events


def simulate_membership_period(customer, product_df):

    membership_months = get_membership_duration(customer)

    current_month = customer["join_date"]

    events = []

    for _ in range(membership_months):

        monthly_events = generate_monthly_visits(
            customer,
            current_month, product_df
        )

        events.extend(monthly_events)

        current_month += DateOffset(months=1)

        membership_end = current_month

    return events, membership_end

def should_renew(customer):
    probability = RENEWAL_PROBABILITY[customer["persona"]
    ]

    return random.random() < probability

def get_renewal_date(membership_end):
    renewal_delay = random.randint(*RENEWAL_DELAY)
    return membership_end + timedelta(days=renewal_delay)

def simulate_customer(customer, product_df):

    events = []
    membership_start = customer["join_date"]

    while membership_start < END_DATE :

        customer["join_date"] = membership_start 

        events.append(
        create_event(
            event_date=customer["join_date"],
            customer_id=customer["customer_id"],
            event_type="Membership",
            product_id=customer["membership_product_id"],
            payment_method=customer["preferred_payment"]
        )
    )
        
        period_events, membership_end = simulate_membership_period(customer, product_df)

        events.extend(period_events)

        if not should_renew(customer):
            break

        membership_start = get_renewal_date(membership_end)


    events.sort(key=lambda x: x["event_date"])

    return events

    



