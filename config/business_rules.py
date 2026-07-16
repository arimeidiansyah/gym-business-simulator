"""
Business Rules
"""

# =====================================================
# REVENUE MIX
# =====================================================

REVENUE_MIX = {
    "Membership": 0.80,
    "PT": 0.12,
    "Merchandise": 0.04,
    "Supplement": 0.04,
}

# =====================================================
# MEMBERSHIP DISTRIBUTION
# =====================================================

MEMBERSHIP_DISTRIBUTION = {
    "Monthly": 45,
    "Quarterly": 30,
    "Semi Annual": 15,
    "Annual": 10
}

# =====================================================
# DEMOGRAPHIC
# =====================================================

GENDER_DISTRIBUTION = {
    "Male": 61.33,
    "Female": 38.67
}

CITY_DISTRIBUTION = {
    "Bekasi": 45,
    "Jakarta": 25,
    "Depok": 10,
    "Bogor": 10,
    "Tangerang": 10
}

AGE_DISTRIBUTION = {
    (18, 24): 25,
    (25, 34): 45,
    (35, 44): 20,
    (45, 54): 8,
    (55, 65): 2
}