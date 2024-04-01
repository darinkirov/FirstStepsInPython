chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50

chicken = int(input())
fish = int(input())
vegan = int(input())

sum_chicken = chicken*chicken_menu
sum_fish = fish*fish_menu
sum_vegan = vegan*vegan_menu
total_sum_menu = sum_chicken + sum_fish + sum_vegan
sum_desert = total_sum_menu*20/100
total_sum_order = total_sum_menu + sum_desert + delivery
print(total_sum_order)