import pandas as pd
from pathlib import Path


def generate_product_dimension():
    """
    Read product master data and export it to Excel.
    """

    project_root = Path(__file__).resolve().parent.parent

    input_file = project_root / "data" / "product_master.csv"
    output_file = project_root / "output" / "dim_product.csv"

    df = pd.read_csv(input_file)

    df.to_csv(output_file, index=False)

    print(f"✅ Product dimension created : {len(df)} rows")