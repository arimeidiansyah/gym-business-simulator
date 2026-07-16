# Project Context

> This document serves as the development handbook for the Gym Business Simulator project.
>
> Unlike `README.md`, which introduces the project to other people, this document records the project's architecture, business decisions, design philosophy, and development progress.
>
> Before continuing development after a long break, always read this document first.

---

# Project Overview

## Objective

Gym Business Simulator is a Python project that simulates the operation of a commercial gym and generates realistic business datasets for analytics purposes.

The objective is not to randomly generate transactions.

Instead, every dataset is produced through business simulation, where customer behaviour creates business events naturally.

The generated datasets will be used for:

- Power BI Dashboard
- SQL Analysis
- Data Analytics Portfolio
- GitHub Portfolio
- Business Intelligence Demonstration

---

# Why This Project Exists

The original idea was to generate a gym dataset directly using AI.

Although AI generated data very quickly, the resulting datasets were unrealistic.

Some common issues included:

- Random customer purchases
- Unrealistic visit frequency
- No membership lifecycle
- No relationship between customer behaviour and transactions

Rather than continuously fixing generated data, the decision was made to simulate the business process itself.

The dataset becomes the output of the simulation.

Business Process → Dataset

instead of

Random Dataset → Try to Make It Look Realistic

---

# Project Philosophy

This project follows several core principles.

## Business Before Code

Business rules are designed first.

Implementation comes afterwards.

The goal is to understand how the business operates before writing Python.

---

## Customer Behaviour Drives Transactions

Transactions should never appear randomly.

Correct business flow:

Customer

↓

Purchase Membership

↓

Visit Gym

↓

Additional Purchases

Incorrect flow:

Generate Random Transactions

↓

Hope They Look Realistic

---

## Simplicity Over Complexity

When multiple approaches exist, choose the simplest design that still produces believable business behaviour.

Avoid unnecessary complexity.

Avoid premature optimization.

---

## Realism Over Perfection

This simulator does not attempt to perfectly replicate every gym.

Instead, it aims to generate believable data that behaves similarly to a real business.

---

## Incremental Development

Small improvements.

Small commits.

Small business rules.

Frequent validation.

---

# Current Version

Version

v1

Current Sprint

Membership Renewal

Project Status

In Development

---

# Current Scope (Version 1)

Included

- Customer generation
- Membership purchase
- Monthly visit simulation
- Supplement purchase
- Merchandise purchase
- Personal Training purchase
- Membership renewal
- Event Log generation

Not Included

- Gym occupancy
- Capacity limitation
- Waiting list
- Customer freeze
- Referral program
- Trainer scheduling
- Marketing campaign
- Customer churn prediction

These belong to future versions.

---

# Business Flow

Customer Created

↓

Purchase Membership

↓

Become Active Member

↓

Monthly Visits

↓

Possible Purchases

• Supplement

• Merchandise

• Personal Training

↓

Membership Expired

↓

Renewal Decision

↓

Purchase Membership Again

↓

Repeat Customer Lifecycle

---

# Customer Personas

Current personas

- Casual
- Fitness Enthusiast
- Premium
- Corporate
- Dormant

Persona influences:

- Visit frequency
- Purchase probability
- Renewal probability
- Payment behaviour

Version 1 assigns persona during customer generation.

Future versions may infer persona automatically based on customer behaviour.

---

# Simulation Period

Observation Window

2024-01-01

↓

2026-12-31

Customer Acquisition Window

2024-01-01

↓

2025-12-31

Reason

Customers joining at the end of 2026 would not generate enough activity for meaningful analysis.

Year 2026 primarily exists to observe renewals and customer lifecycle.

---

# Current Data Pipeline

The simulator intentionally produces one raw chronological event log.

Business Simulation

↓

Raw Event Log

↓

Transformation

↓

Fact Visit

+

Fact Transaction

↓

Power BI Dashboard

The Event Log is not the final analytical dataset.

It serves as the source for downstream transformations.

This separation keeps simulation logic independent from reporting logic.

---

# Event Log

The Event Log records every business activity chronologically.

Current Event Types

- Membership
- Visit
- Supplement
- Merchandise
- Personal Training

Future Event Types

- Locker Rental
- Freeze Membership
- Referral
- Cancellation

Membership renewal is represented as another Membership event with a renewal indicator rather than introducing a separate event type.

---

# Dimensions

Current dimensions

- dim_customer
- dim_membership
- dim_product

Future dimensions may include

- dim_employee
- dim_trainer
- dim_branch

Only add new dimensions when they provide analytical value.

---

# Revenue Assumptions

Current revenue mix

Membership

80%

Personal Training

11%

Merchandise

5%

Supplement

2%

Locker

2%

These values are business assumptions.

They may be adjusted after validating the generated data.

---

# Architecture Decisions

## Why One Event Log?

Instead of generating multiple fact tables directly, the simulator first produces one chronological event log.

Advantages

- Easier debugging
- Easier validation
- Business history is preserved
- Flexible transformations
- Similar to event-driven systems

Fact tables are generated from the event log.

They are not produced directly by the simulator.

---

# Coding Principles

Keep functions small.

One function should solve one problem.

Separate business rules from implementation.

Store configurable values inside config files.

Avoid hardcoded values.

Avoid magic numbers.

Prioritize readability over clever code.

Commit every meaningful milestone.

---

# Current Progress

Completed

✔ Membership Dimension

✔ Product Dimension

✔ Customer Dimension

✔ Event Generator

✔ Visit Simulation

✔ Purchase Simulation

✔ README

In Progress

⏳ Membership Renewal

Upcoming

- Fact Visit Generator
- Fact Transaction Generator
- Power BI Dashboard
- Data Validation
- Documentation

---

# Future Ideas (Parking Lot)

The following ideas have been intentionally postponed.

Do not implement before Version 1 is complete.

- Dynamic customer acquisition
- Gym occupancy simulation
- Capacity management
- Peak hour simulation
- Customer churn model
- Referral system
- Marketing campaign
- Machine Learning persona classification
- Behaviour-based customer segmentation
- Revenue forecasting

These ideas remain valuable but should never interrupt Version 1 development.

---

# Lessons Learned

The hardest part of this project is not writing Python.

The hardest part is designing business rules that produce believable data.

Code becomes relatively straightforward once the business logic has been clearly defined.

This project demonstrates analytical thinking as much as programming ability.

---

# Development Workflow

Every feature follows the same sequence.

1. Discuss the business process.
2. Define business rules.
3. Review edge cases.
4. Design the implementation.
5. Write code.
6. Validate generated data.
7. Commit.
8. Continue.

Business discussion always comes before implementation.

---

# Resume Checklist

If development resumes after a long break:

1. Read README.md
2. Read project_context.md
3. Review latest Git commits
4. Review the current sprint
5. Run the generator
6. Validate output
7. Continue from the current sprint

Avoid introducing new features before completing the current sprint unless a bug blocks progress.

---

# Long-Term Vision

Version 1

Generate realistic business datasets.

Version 2

Introduce adaptive customer behaviour where personas emerge naturally from customer activities instead of being assigned during customer creation.

Version 3

Expand into operational simulation, including occupancy, capacity planning, scheduling, and advanced business scenarios.

The long-term goal is to build a reusable business simulation engine capable of generating realistic datasets for analytics, dashboard development, SQL practice, and portfolio projects.

---

# Personal Reminder

Do not chase complexity.

A realistic, well-documented, and completed Version 1 is far more valuable than an unfinished simulator with dozens of advanced ideas.

Finish what is currently being built before starting the next feature.