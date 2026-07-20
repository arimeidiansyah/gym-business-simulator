import pandas as pd

from config.settings import OUTPUT_FOLDER

def generate_fact_visit():

    event_log = pd.read_csv(
        OUTPUT_FOLDER / "fact_event_log.csv",
        parse_dates=["event_date", "check_in", "check_out"]
    )
    
    visit_df = event_log[event_log["event_type"]=="Visit"].copy()

    visit_df = visit_df[
        [
            "customer_id",
            "event_date",
            "check_in",
            "check_out",
            "duration_minutes"
        ]
    ]

    visit_df.rename(
        columns={
            "event_date": "visit_date",
            "duration_minutes": "visit_minutes"
        },
        inplace=True
    )

    visit_df.insert(
        0,
        "visit_id",
        [
            f"VIS{i:06d}"
            for i in range(
                1, len(visit_df) + 1)
        ]
    )

    visit_df.to_csv(
        OUTPUT_FOLDER / "fact_visit.csv",
        index=False
    )

    print(f"✅ Fact Visit : {len(visit_df)} rows")

    print(visit_df["visit_id"].duplicated().sum())
    print(visit_df["customer_id"].isna().sum())
    print(visit_df["visit_minutes"].isna().sum())