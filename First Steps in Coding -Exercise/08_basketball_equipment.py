yearly_price_train = int(input())

price_shoes = yearly_price_train - yearly_price_train*40/100
price_outfit = price_shoes - price_shoes*20/100
price_ball = price_outfit*1/4
price_accesoaries = price_ball*1/5
total_price = yearly_price_train + price_outfit + price_shoes + price_ball + price_accesoaries
print(total_price)