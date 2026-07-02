"""
Purchase Behaviour per Persona
Probability of buying additional products/services.
"""

PERSONA_PURCHASE_RULES = {

    "Casual": {
        "pt": 0.03,
        "supplement": 0.12,
        "merchandise": 0.05,
        "locker": 0.02
    },

    "Fitness Enthusiast": {
        "pt": 0.25,
        "supplement": 0.45,
        "merchandise": 0.12,
        "locker": 0.05
    },

    "Premium": {
        "pt": 0.55,
        "supplement": 0.35,
        "merchandise": 0.20,
        "locker": 0.20
    },

    "Corporate": {
        "pt": 0.10,
        "supplement": 0.15,
        "merchandise": 0.05,
        "locker": 0.05
    },

    "Dormant": {
        "pt": 0.00,
        "supplement": 0.03,
        "merchandise": 0.01,
        "locker": 0.00
    }

}