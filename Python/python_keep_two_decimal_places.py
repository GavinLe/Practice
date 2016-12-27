from decimal import Decimal
reader = [5,4.2,5.8,0.234,1.0] 
rowvals = [Decimal(str(x)).quantize(Decimal('0.00')) for x in reader]
print rowvals 