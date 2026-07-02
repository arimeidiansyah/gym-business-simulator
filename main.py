from dimensions.dim_membership import generate_membership_dimension
from dimensions.dim_product import generate_product_dimension
from generators.customer_generator import generate_customers
from generators.transaction_generator import generate_customer_events


def main():

    print("=" * 50)
    print("GYM BUSINESS DATA GENERATOR")
    print("=" * 50)

    generate_membership_dimension()

    generate_product_dimension()

    generate_customers()

    generate_customer_events()

    print("\nFinished Successfully")


if __name__ == "__main__":
    main()