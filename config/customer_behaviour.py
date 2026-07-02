"""
Customer Behaviour Rules
"""

CUSTOMER_BEHAVIOUR = {

    "Casual": {

        "visit_per_month": (2, 5),

        "renew_rate": 0.40,

        "pt_interest": 0.05,

        "supplement_interest": 0.10,

        "merchandise_interest": 0.08,

        "locker_interest": 0.02
    },

    "Fitness Enthusiast": {

        "visit_per_month": (10, 16),

        "renew_rate": 0.80,

        "pt_interest": 0.35,

        "supplement_interest": 0.50,

        "merchandise_interest": 0.12,

        "locker_interest": 0.05
    },

    "Premium": {

        "visit_per_month": (12, 20),

        "renew_rate": 0.90,

        "pt_interest": 0.50,

        "supplement_interest": 0.40,

        "merchandise_interest": 0.20,

        "locker_interest": 0.15
    },

    "Corporate": {

        "visit_per_month": (6, 10),

        "renew_rate": 0.75,

        "pt_interest": 0.15,

        "supplement_interest": 0.20,

        "merchandise_interest": 0.05,

        "locker_interest": 0.10
    },

    "Dormant": {

        "visit_per_month": (0, 2),

        "renew_rate": 0.10,

        "pt_interest": 0.01,

        "supplement_interest": 0.03,

        "merchandise_interest": 0.01,

        "locker_interest": 0.00
    }

}