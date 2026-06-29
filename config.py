"""
Configuration File
Gym Business Data Generator

All business parameters should be configured here.
"""
from pathlib import Path
from datetime import datetime

# ==========================================================
# GENERAL
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FOLDER = BASE_DIR / "output"

RANDOM_SEED = 42

START_DATE = datetime(2024, 7, 1)
END_DATE = datetime(2026, 6, 30)

TOTAL_CUSTOMERS = 3000
TARGET_TRANSACTIONS = 30000

# ==========================================================
# REVENUE MIX (Target Percentage)
# ==========================================================

REVENUE_TARGET = {
    "Membership": 0.80,
    "Personal Training": 0.12,
    "Merchandise": 0.04,
    "Supplement": 0.02,
    "Locker Rental": 0.02
}

# ==========================================================
# CUSTOMER PERSONA DISTRIBUTION
# ==========================================================

CUSTOMER_PERSONA = {
    "Casual": 0.40,
    "Fitness Enthusiast": 0.25,
    "Premium": 0.15,
    "Corporate": 0.10,
    "Dormant": 0.10
}

# ==========================================================
# PAYMENT METHODS
# ==========================================================

PAYMENT_METHODS = [
    "Cash",
    "QRIS",
    "Credit Card",
    "Debit Card",
    "Bank Transfer",
    "E-Wallet"
]

# ==========================================================
# MEMBERSHIP TYPES
# ==========================================================

MEMBERSHIP_TYPES = {
    "Monthly": {
        "duration": 30,
        "price": 500000
    },
    "Quarterly": {
        "duration": 90,
        "price": 1350000
    },
    "Semi Annual": {
        "duration": 180,
        "price": 2400000
    },
    "Annual": {
        "duration": 365,
        "price": 4500000
    }
}

# ==========================================================
# PERSONAL TRAINING
# ==========================================================

PT_PACKAGES = {
    "PT 5 Sessions": 850000,
    "PT 10 Sessions": 1600000,
    "PT 20 Sessions": 3000000
}

# ==========================================================
# SUPPLEMENTS
# ==========================================================

SUPPLEMENTS = {
    "Whey Protein": 650000,
    "Creatine": 350000,
    "BCAA": 450000,
    "Pre Workout": 500000,
    "Protein Bar": 35000
}

# ==========================================================
# MERCHANDISE
# ==========================================================

MERCHANDISE = {
    "Gym T-Shirt": 180000,
    "Gym Bottle": 120000,
    "Gym Towel": 90000,
    "Gym Bag": 350000,
    "Cap": 150000
}

# ==========================================================
# LOCKER
# ==========================================================

LOCKER = {
    "Monthly Locker": 100000,
    "Annual Locker": 900000
}