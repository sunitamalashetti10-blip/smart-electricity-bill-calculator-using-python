# Smart Electricity Bill Calculator

A beginner-friendly Python console program that collects customer details,
checks the electricity units entered, calculates the bill, and prints a clear
bill summary. It uses only Python's built-in features.

## How to run

Run `smart_electricity_bill_calculator.py` with Python 3:

```text
python smart_electricity_bill_calculator.py
```

## Program flow

1. `main()` calls `get_customer_details()` to ask for the customer's name,
	customer ID, and electricity units consumed.
2. The units are converted to a number. If the entry is not numeric or is
	negative, the program displays an error and asks again.
3. `main()` passes the units to `calculate_bill()`. The energy charge is
	progressive: the first 100 units cost Rs. 2 per unit, units 101-200 cost
	Rs. 4 per unit, units 201-500 cost Rs. 6 per unit, and each unit above 500
	costs Rs. 8. A fixed service charge of Rs. 100 is added.
4. `calculate_bill()` returns the energy charge, service charge, and final
	amount.
5. `main()` passes the customer details and returned amounts to
	`display_bill()`, which prints the formatted electricity bill.

The supplied slab list says both "201 to 5000" and "above 500". This program
interprets the first range as 201-500 so the slabs are continuous and do not
overlap.