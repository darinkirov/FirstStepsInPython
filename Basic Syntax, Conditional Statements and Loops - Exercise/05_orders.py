number_of_orders = int(input())
price_total = 0
for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days <  1 or days > 31:
        continue
    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    price = price_per_capsule*days*capsules_needed_per_day
    price_total += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total : ${price_total:.2f}")