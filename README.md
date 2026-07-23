#  Event-Driven Gym Business Simulator

A Python-based synthetic data generator that simulates the operations of a commercial fitness center using configurable business rules and customer behavior models.

---

# Why This Project?

Many data analytics portfolios rely on public datasets that are already clean, static, and lack realistic business processes.

This project was created to solve that problem by generating synthetic business data that mimics how a real gym operates.

Instead of randomly generating rows, the simulator models customer journeys, memberships, visits, purchases, renewals, and churn using configurable business rules.

The generated datasets can then be used for SQL analysis, Power BI dashboards, business analysis, and data visualization projects.

---

# Project Objectives

This project aims to:

- Build realistic synthetic business datasets.
- Simulate customer behavior using event-driven logic.
- Practice dimensional data modeling.
- Produce analytics-ready fact and dimension tables.
- Demonstrate Business Analyst and Data Analyst skills.

---

# How It Works

Every customer follows a business journey.

```text
New Customer
      │
      ▼
Purchase Membership
      │
      ▼
Visit Gym
      │
      ├───────────────┐
      ▼               ▼
Buy Product      Personal Training
      │
      ▼
Membership Expired
      │
      ▼
Renew or Churn
```

Instead of creating random transactions, every record is generated from this customer lifecycle.

---

# Technologies

- Python
- Pandas
- NumPy
- Faker
- Git
- Power BI (for analysis)
- VS Code

---

# Project Structure

```
gym-business-simulator
│
├── config/
├── data/
├── dimensions/
├── generators/
├── output/
├── utils/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Generated Dataset

## Dimension Tables

- dim_customer
- dim_membership
- dim_product

## Fact Tables

- fact_event_log
- fact_visit
- fact_transaction

These tables follow a dimensional modeling approach and are ready to be used for analytical reporting.

---

# Business Rules

The simulator currently supports:

- Customer personas
- Membership preferences
- Visit frequency
- Membership renewal probability
- Product purchase probability
- Payment behavior
- Customer churn

All business rules are configurable through the `config` module.

---

# Example Use Cases

The generated datasets can be used for:

- Power BI Dashboard
- SQL Portfolio
- Customer Segmentation
- Revenue Analysis
- Membership Analysis
- Cohort Analysis
- Visit Pattern Analysis
- Business Performance Reporting

---

# Future Improvements

Version 2 is planned to include:

- Dynamic customer acquisition
- State-based customer journey
- Marketing campaign simulation
- Employee dimension
- Operational cost simulation
- Profit & Loss simulation
- Multi-branch support
- Seasonal customer behavior

---

# Author

**Ari Meidiansyah**

Business Analyst & Data Analyst Portfolio Project
