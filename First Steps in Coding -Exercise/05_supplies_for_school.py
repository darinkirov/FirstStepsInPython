count_pen = int(input())
count_markers = int(input())
detergent_liters = int(input())
discount = int(input())
price_pen = 5.80
price_markers = 7.20
price_detergent = 1.20

total_price_pen = count_pen * price_pen
total_price_markers = count_markers * price_markers
total_price_detergent = detergent_liters * price_detergent
total_sum = total_price_pen + total_price_markers + total_price_detergent
total_sum =  format(total_sum - (total_sum * discount/100) , ".2f")
print(total_sum)