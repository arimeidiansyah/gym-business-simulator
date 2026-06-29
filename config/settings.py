"""
Project Settings
"""
from pathlib import Path
from datetime import datetime

# =====================================================
# PROJECT
# =====================================================

PROJECT_NAME = "Gym Business Simulator"

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FOLDER = BASE_DIR / "output"


# =====================================================
# DATASET SETTINGS
# =====================================================

TOTAL_CUSTOMERS = 3000

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)

# Random seed agar hasil generator konsisten
RANDOM_SEED = 42

# =====================================================
# OUTPUT
# =====================================================

OUTPUT_FOLDER = "output"