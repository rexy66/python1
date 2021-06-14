'''

calculate handling fee based on the firm you trade with
'''
import math

code = int(input("What stock are you trading?"))
lot_size = int(input("How many shares in one lot?"))
lots = int(input("How many lots are you trading?"))
pur_price=float(input("The purchase price?"))
cost = lot_size * pur_price * lots
print (f"cost is : {cost}")

brokeragefee = float(cost * 0.0025)
if brokeragefee > 100:
    brokeragefee = 100

stampduty = math.ceil(cost * 0.001)
translevy = math.ceil(cost * 0.000027)
hkexfee = math.ceil(cost * 0.00005)

print (f"Brokerage fee: {brokeragefee}")
print (f"Stamp duty: {stampduty}")
print (f"Transaction levy:{translevy}")
print (f"Hkex fee: {hkexfee}")
print (f"total transaction fee")
