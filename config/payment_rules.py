"""
Payment Behaviour Rules
"""

PAYMENT_BEHAVIOUR = {

    "Casual": {

        "QRIS": 45,
        "E-Wallet": 35,
        "Cash": 20
    },

    "Fitness Enthusiast": {

        "QRIS": 25,
        "E-Wallet": 30,
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
        "QRIS": 30,
        "E-Wallet": 30
    }

}