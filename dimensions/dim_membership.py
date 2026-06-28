import pandas as pd
from pathlib import Path


def generate_membership_dimension():
    """
    Read membership master data and export it to Excel.
    """

    project_root = Path(__file__).resolve().parent.parent

    input_file = project_root / "data" / "membership_master.csv"
    output_file = project_root / "output" / "dim_membership.xlsx"

    df = pd.read_csv(input_file)

    df.to_excel(output_file, index=False)

    print(f"✅ Membership dimension created: {output_file}")