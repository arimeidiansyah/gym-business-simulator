from dimensions.dim_membership import generate_membership_dimension
from dimensions.dim_product import generate_product_dimension
from generators.customer_generator import generate_customers
from generators.event_generator import generate_events
from generators.visit_generator import generate_fact_visit
from generators.transaction_generator import generate_fact_transaction



def main():

    print("=" * 50)
    print("GYM BUSINESS DATA GENERATOR")
    print("=" * 50)

    generate_membership_dimension()

    generate_product_dimension()

    generate_customers()

    generate_events()

    generate_fact_visit()

    generate_fact_transaction()

    print("\nFinished Successfully")

if __name__ == "__main__":
    main()

