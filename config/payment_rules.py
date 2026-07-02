"""
Payment Behaviour Rules
"""

PAYMENT_BEHAVIOUR = {

    "Casual": {

        "QRIS": 80,
        "Cash": 20
    },

    "Fitness Enthusiast": {

        "QRIS": 55,
        "Credit Card": 25,
        "Bank Transfer": 20
    },

    "Premium": {

        "Credit Card": 60,
        "Bank Transfer": 30,
        "QRIS": 10
    },

    "Corporate": {

        "Bank Transfer": 80,
        "Credit Card": 20
    },

    "Dormant": {

        "Cash": 40,
        "QRIS": 60
    }

}