"""Pizza Order Calculator: prices a pizza order from size, toppings and delivery distance."""

import math
import sys

BASE_PRICES = {"small": 8, "large": 12}
TOPPING_PRICE = 1
DELIVERY_BASE_FEE = 2
FREE_DELIVERY_MILES = 5
PRICE_PER_EXTRA_MILE = 1


def delivery_fee(distance):
    """Return the delivery fee for a distance in miles (0 means pickup)."""
    if distance == 0:
        return 0
    if distance <= FREE_DELIVERY_MILES:
        return DELIVERY_BASE_FEE
    # Fractional extra miles are charged proportionally.
    return DELIVERY_BASE_FEE + (distance - FREE_DELIVERY_MILES) * PRICE_PER_EXTRA_MILE


def main():
    pizza_size = input("Pizza size (small or large): ").strip().lower()
    if pizza_size not in BASE_PRICES:
        sys.exit("Invalid pizza size. Please choose small or large.")

    try:
        toppings = int(input("Number of additional toppings: "))
        distance = float(input("Delivery distance in miles (0 for pickup): "))
    except ValueError:
        sys.exit("Please enter numbers for toppings and distance.")

    if toppings < 0 or distance < 0 or not math.isfinite(distance):
        sys.exit("Toppings and distance must be non-negative numbers.")

    base_cost = BASE_PRICES[pizza_size]
    topping_cost = toppings * TOPPING_PRICE
    fee = delivery_fee(distance)
    total_cost = base_cost + topping_cost + fee

    print(f"\nPizza cost: ${base_cost:.2f}")
    print(f"Toppings cost: ${topping_cost:.2f}")
    print(f"Delivery fee: ${fee:.2f}")
    print(f"Total order cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
