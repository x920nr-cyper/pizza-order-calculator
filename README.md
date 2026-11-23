# Pizza Order Calculator

A small Python command-line program that works out the total cost of a pizza order.

## Pricing rules

| Item | Cost |
|---|---|
| Small pizza | $8 |
| Large pizza | $12 |
| Each extra topping | $1 |
| Pickup (0 miles) | Free |
| Delivery up to 5 miles | $2 |
| Delivery over 5 miles | $2 + $1 per extra mile |

## Run it

```bash
python pizza_calculator.py
```

## Example

```
Pizza size (small or large): large
Number of additional toppings: 3
Delivery distance in miles (0 for pickup): 7

Pizza cost: $12.00
Toppings cost: $3.00
Delivery fee: $4.00
Total order cost: $19.00
```

## What I practised

- Reading and converting user input
- `if` / `elif` / `else` decisions
- Input validation
- Formatted output with f-strings

Built as part of my Moringa School coursework.
