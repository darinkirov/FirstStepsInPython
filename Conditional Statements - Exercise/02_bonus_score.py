number = int(input())

total_bonus = 0
total_sum = number + total_bonus

if number <= 100:
    total_bonus += 5
if number > 100 and number < 1000:
    total_bonus += number * 20/100
if number > 1000:
    total_bonus += number * 10/100
if number % 2 == 0:
    total_bonus += 1
if number % 10 == 5:
    total_bonus += 2

total_sum = number + total_bonus

print(total_bonus)
print(total_sum)