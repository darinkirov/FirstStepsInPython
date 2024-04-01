price_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_tinder = int(input())
count_minions = int(input())
count_truck = int(input())

puzzles = 2.60
dolls = 3
tinder = 4.10
minions = 8.20
truck = 2
total_sum = count_puzzles*puzzles + count_dolls*dolls + count_tinder*tinder + count_minions*minions + count_truck*truck
total_sum_toys = count_minions + count_truck + count_tinder + count_dolls + count_puzzles
if total_sum_toys >= 50:
    total_sum = total_sum * 75/100

total_sum *= 90/100
if total_sum >= price_trip:
    print(f"Yes! {total_sum-price_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_trip-total_sum:.2f} lv needed.")