SERVICE_CHARGE = 100.0


def get_customer_details():
    """Ask for the customer's details and validate the consumed units."""
    customer_name = input("Enter customer name: ").strip()
    customer_id = input("Enter customer ID: ").strip()

    while True:
        try:
            units_consumed = float(input("Enter electricity units consumed: "))
            if units_consumed < 0:
                print("Units consumed cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units_consumed
        except ValueError:
            print("Please enter a valid number of units.")


def calculate_bill(units_consumed):
    """Calculate progressive energy charges and the final bill amount."""
    if units_consumed <= 100:
        energy_charge = units_consumed * 2
    elif units_consumed <= 200:
        energy_charge = (100 * 2) + ((units_consumed - 100) * 4)
    elif units_consumed <= 500:
        energy_charge = (100 * 2) + (100 * 4) + ((units_consumed - 200) * 6)
    else:
        energy_charge = (
            (100 * 2)
            + (100 * 4)
            + (300 * 6)
            + ((units_consumed - 500) * 8)
        )

    service_charge = SERVICE_CHARGE
    final_amount = energy_charge + service_charge
    return energy_charge, service_charge, final_amount


def display_bill(customer_name, customer_id, units_consumed, energy_charge,
                 service_charge, final_amount):
    """Print a formatted electricity bill."""
    print("\n" + "=" * 40)
    print("           ELECTRICITY BILL")
    print("=" * 40)
    print(f"Customer name       : {customer_name}")
    print(f"Customer ID         : {customer_id}")
    print(f"Units consumed      : {units_consumed:g}")
    print("-" * 40)
    print(f"Energy charge       : Rs. {energy_charge:.2f}")
    print(f"Service charge      : Rs. {service_charge:.2f}")
    print("-" * 40)
    print(f"Final amount        : Rs. {final_amount:.2f}")
    print("=" * 40)


def main():
    customer_name, customer_id, units_consumed = get_customer_details()
    energy_charge, service_charge, final_amount = calculate_bill(units_consumed)
    display_bill(customer_name, customer_id, units_consumed, energy_charge,
                 service_charge, final_amount)


if __name__ == "__main__":
    main()