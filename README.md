# Gym Business Simulator

## Overview

Gym Business Simulator is a Python project that simulates the daily operations of a gym and generates business datasets for analytics purposes.

The initial idea was to generate a gym dataset directly using AI. While it produced data quickly, the result was too random and did not reflect how a gym business actually operates. This project was created to simulate the business process first, allowing the generated data to follow more realistic customer behavior.

The project is being developed as part of my Data Analytics portfolio.

---

## Current Progress

Completed

* Customer Generator
* Membership Dimension
* Product Dimension
* Event Log Generator
* Visit Simulation
* Visit Timestamp
* Supplement Purchase Event
* Merchandise Purchase Event
* Personal Training Purchase Event

Currently in Progress

* Membership Renewal
* Fact Visit
* Fact Transaction

Planned

* SQL Analysis
* Power BI Dashboard
* Project Documentation

---

## Business Flow

The simulator currently follows this business process:

```text
Customer
    ↓
Membership
    ↓
Gym Visit
    ↓
Purchase Event
    ↓
Event Log
```

Instead of generating transactions randomly, every purchase is generated from an actual customer visit.

---

## Current Business Rules

Some of the business rules implemented in the current version include:

* Customers are assigned different personas.
* Each persona has different visit frequency.
* Visit events include check-in and check-out timestamps.
* Supplement and merchandise purchases may occur during a visit.
* Personal Training can only be purchased once within a membership period.
* Payment methods follow each customer's preference.

These rules will continue to evolve as the simulator becomes more realistic.

---

## Project Structure

```text
gym-business-simulator/

├── config/
├── dimensions/
├── generators/
├── output/
├── utils/
├── main.py
└── README.md
```

---

## Technology

* Python
* Pandas
* Git
* GitHub

---

## Version

Current Version: **v1 (Work in Progress)**

This repository is actively being developed. New features and business rules will be added as the project evolves.
