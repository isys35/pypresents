from decimal import Decimal, ROUND_HALF_EVEN
 
 
number = Decimal("10.025")      # 2 - ближайшее четное число
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.02
 
number = Decimal("10.035")      # 4 - ближайшее четное число
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.04