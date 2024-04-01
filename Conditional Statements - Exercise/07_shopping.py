budget = float(input())
count_video_cards = int(input())
count_cpu = int(input())
count_ram = int(input())

price_video_card = 250
total_sum_video_card = price_video_card * count_video_cards
price_cpu = total_sum_video_card * 35/100
price_ram = total_sum_video_card * 10/100

total_sum_cpu = count_cpu * price_cpu
total_sum_ram = count_ram * price_ram

total_sum = total_sum_video_card + total_sum_cpu + total_sum_ram

if count_video_cards > count_cpu:
    total_sum *= 85/100

left_money = abs(total_sum - budget)
if total_sum <= budget:
    print(f"You have {left_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_money:.2f} leva more!")