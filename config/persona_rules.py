"""
Customer Persona Rules
"""

PERSONA_PROFILE = {

    "Casual": {

        "renewal_probability": 0.45,
        "visit_per_month": (2, 6),

        "pt_probability": 0.08,
        "supplement_probability": 0.10,
        "merchandise_probability": 0.10,
        "locker_probability": 0.02,

        "membership_preference": [
            "Monthly",
            "Quarterly"
        ]
    },

    "Fitness Enthusiast": {

        "renewal_probability": 0.75,
        "visit_per_month": (10, 18),

        "pt_probability": 0.45,
        "supplement_probability": 0.55,
        "merchandise_probability": 0.15,
        "locker_probability": 0.20,

        "membership_preference": [
            "Quarterly",
            "Semi Annual"
        ]
    },

    "Premium": {

        "renewal_probability": 0.90,
        "visit_per_month": (12, 22),

        "pt_probability": 0.80,
        "supplement_probability": 0.70,
        "merchandise_probability": 0.25,
        "locker_probability": 0.80,

        "membership_preference": [
            "Annual"
        ]
    },

    "Corporate": {

        "renewal_probability": 0.65,
        "visit_per_month": (4, 8),

        "pt_probability": 0.20,
        "supplement_probability": 0.15,
        "merchandise_probability": 0.08,
        "locker_probability": 0.10,

        "membership_preference": [
            "Monthly",
            "Quarterly"
        ]
    },

    "Dormant": {

        "renewal_probability": 0.20,
        "visit_per_month": (0, 2),

        "pt_probability": 0.02,
        "supplement_probability": 0.03,
        "merchandise_probability": 0.02,
        "locker_probability": 0.00,

        "membership_preference": [
            "Monthly"
        ]
    }

}

# =====================================================
# PERSONA DISTRIBUTION
# =====================================================

PERSONA_DISTRIBUTION = {
    "Casual": 40,
    "Fitness Enthusiast": 25,
    "Premium": 15,
    "Corporate": 10,
    "Dormant": 10
}