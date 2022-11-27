from decimal import Decimal
 
number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)

number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))       # 0.56
 
number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))