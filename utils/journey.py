import random
from datetime import datetime,timedelta

from utils.event import create_event
from config.customer_behaviour import CUSTOMER_BEHAVIOUR

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

def generate_monthly_visits(customer, month_start, product_df):

    behaviour = CUSTOMER_BEHAVIOUR[customer["persona"]]

    min_visits, max_visits = behaviour["visit_per_month"]

    total_visits = random.randint(min_visits, max_visits)

    visit_days = sorted(
        random.sample(range(1, 29), total_visits)
    )

    events = []

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

        current_month = current_month + DateOffset(months=1)

    return events

def simulate_customer(customer, product_df):

    events = []

    membership_name = customer["membership_preference"] + " Membership"

    events.append(
        create_event(
            event_date=customer["join_date"],
            customer_id=customer["customer_id"],
            event_type="Membership",
            product_id=membership_name,
            payment_method=customer["preferred_payment"]
        )
    )

    period_events = simulate_membership_period(customer, product_df)

    events.extend(period_events)

    events.sort(key=lambda x: x["event_date"])

    return events
