import random
# Given some values to computer a discount price when a minimum amount of an item are sold

MINIMUM_AMOUNT_FOR_DISCOUNT = 100
NORMAL_PRICE = 25
DISCOUNT_PRICE = 20

number_sold = random.randint(50,150)

if number_sold > MINIMUM_AMOUNT_FOR_DISCOUNT: 
  total = number_sold * DISCOUNT_PRICE 
  label = f'Final Total: {total}' 
  print (label)

else: 
  total = number_sold * NORMAL_PRICE 
  label = f'Final Total: {total}' 
  print (label)
