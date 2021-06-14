'''

calculate handling fee based on the firm you trade with
'''

code = int(input("What stock are you trading?"))
lot_size = int(input("How many shares in one lot?"))
lots = int("How many lots are you trading?")
amount = int(input("how many shares?"))
pur_price = float(input("The purchase price?"))
cost = amount * pur_price
print (f"cost is : {cost}")

0.25% brokerage fee (min 100)
0.10 % stamp duty
0.0027% transaction levy
0.005% hkex tranastion fee
